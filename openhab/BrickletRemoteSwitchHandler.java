package org.eclipse.smarthome.binding.tinkerforge.internal.handler;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.concurrent.ConcurrentLinkedQueue;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.function.BiFunction;
import java.util.function.Consumer;
import java.util.function.Supplier;

import com.tinkerforge.BrickletOutdoorWeather;
import com.tinkerforge.BrickletRemoteSwitch;
import com.tinkerforge.BrickletRemoteSwitchV2;
import com.tinkerforge.DefaultActions;
import com.tinkerforge.Device;
import com.tinkerforge.IPConnection;
import com.tinkerforge.TinkerforgeException;

import org.eclipse.jdt.annotation.Nullable;
import org.eclipse.smarthome.config.core.ConfigDescriptionRegistry;
import org.eclipse.smarthome.core.thing.Bridge;
import org.eclipse.smarthome.core.thing.Thing;
import org.eclipse.smarthome.core.thing.ThingUID;
import org.eclipse.smarthome.core.thing.binding.BridgeHandler;
import org.eclipse.smarthome.core.thing.binding.ThingHandler;
import org.eclipse.smarthome.core.thing.binding.builder.BridgeBuilder;
import org.eclipse.smarthome.core.thing.type.ChannelTypeRegistry;

public class BrickletRemoteSwitchHandler extends DeviceHandler implements BridgeHandler {
    @FunctionalInterface
    public interface CheckedConsumer<T> {
        void accept(T t) throws TinkerforgeException;
    }

    public interface RemoteSwitch {
        void switchSocketA(int houseCode, int receiverCode, int switchTo) throws TinkerforgeException;

        void switchSocketB(int address, int unit, int switchTo) throws TinkerforgeException;

        void dimSocketB(int address, int unit, int dimValue) throws TinkerforgeException;

        void switchSocketC(char systemCode, int deviceCode, int switchTo) throws TinkerforgeException;

        void setRepeats(int repeats) throws TinkerforgeException;

        int getSwitchingState() throws TinkerforgeException;

        void addSwitchingDoneListener(AtomicBoolean isSwitching);

        void removeSwitchingDoneListener();
    }

    class BrickletRemoteSwitchWrapper implements RemoteSwitch {
        BrickletRemoteSwitch rs;
        BrickletRemoteSwitch.SwitchingDoneListener listener;

        public BrickletRemoteSwitchWrapper(BrickletRemoteSwitch rs) {
            this.rs = rs;
        }
        @Override
        public void switchSocketA(int houseCode, int receiverCode, int switchTo) throws TinkerforgeException {
            this.rs.switchSocketA(houseCode, receiverCode,switchTo);
        }

        @Override
        public void switchSocketB(int address, int unit, int switchTo) throws TinkerforgeException {
            this.rs.switchSocketB(address, unit, switchTo);
        }

        @Override
        public void dimSocketB(int address, int unit, int dimValue) throws TinkerforgeException {
            this.rs.dimSocketB(address, unit, dimValue);
        }

        @Override
        public void switchSocketC(char systemCode, int deviceCode, int switchTo) throws TinkerforgeException {
            this.rs.switchSocketC(systemCode, deviceCode,switchTo);
        }

        @Override
        public void setRepeats(int repeats) throws TinkerforgeException {
            this.rs.setRepeats(repeats);
        }

        @Override
        public int getSwitchingState() throws TinkerforgeException {
            return this.rs.getSwitchingState();
        }

        @Override
        public void addSwitchingDoneListener(AtomicBoolean isSwitching) {
            listener = () -> isSwitching.set(false);
            this.rs.addSwitchingDoneListener(listener);
        }

        @Override
        public void removeSwitchingDoneListener() {
            this.rs.removeSwitchingDoneListener(listener);
        }
    }

    class BrickletRemoteSwitchV2Wrapper implements RemoteSwitch {
        BrickletRemoteSwitchV2 rs;
        BrickletRemoteSwitchV2.SwitchingDoneListener listener;

        public BrickletRemoteSwitchV2Wrapper(BrickletRemoteSwitchV2 rs) {
            this.rs = rs;
        }
        @Override
        public void switchSocketA(int houseCode, int receiverCode, int switchTo) throws TinkerforgeException {
            this.rs.switchSocketA(houseCode, receiverCode,switchTo);
        }

        @Override
        public void switchSocketB(int address, int unit, int switchTo) throws TinkerforgeException {
            this.rs.switchSocketB(address, unit, switchTo);
        }

        @Override
        public void dimSocketB(int address, int unit, int dimValue) throws TinkerforgeException {
            this.rs.dimSocketB(address, unit, dimValue);
        }

        @Override
        public void switchSocketC(char systemCode, int deviceCode, int switchTo) throws TinkerforgeException {
            this.rs.switchSocketC(systemCode, deviceCode,switchTo);
        }

        @Override
        public void setRepeats(int repeats) throws TinkerforgeException {
            this.rs.setRepeats(repeats);
        }

        @Override
        public int getSwitchingState() throws TinkerforgeException {
            return this.rs.getSwitchingState();
        }

        @Override
        public void addSwitchingDoneListener(AtomicBoolean isSwitching) {
            listener = () -> isSwitching.set(false);
            this.rs.addSwitchingDoneListener(listener);
        }

        @Override
        public void removeSwitchingDoneListener() {
            this.rs.removeSwitchingDoneListener(listener);
        }
    }

    private @Nullable RemoteSwitch remoteSwitch = null;

    public static class Task {
        CheckedConsumer<RemoteSwitch> task;
        Consumer<Boolean> callback;

        public Task(CheckedConsumer<RemoteSwitch> task, Consumer<Boolean> callback) {
            this.task = task;
            this.callback = callback;
        }
    }

    private List<ThingHandler> childHandlers = new ArrayList<>();

    private Queue<Task> tasks = new ConcurrentLinkedQueue<>();
    private AtomicBoolean isSwitching = new AtomicBoolean(true);
    private ScheduledFuture<?> workFuture = null;

    public BrickletRemoteSwitchHandler(Bridge bridge, BiFunction<String, IPConnection, Device> deviceSupplier,
            Supplier<ChannelTypeRegistry> channelTypeRegistrySupplier,
            Supplier<ConfigDescriptionRegistry> configDescriptionRegistrySupplier) {
        super(bridge, deviceSupplier, DefaultActions.class, channelTypeRegistrySupplier,
                configDescriptionRegistrySupplier);
    }

    public void handleTimeout() {
        ((BrickDaemonHandler) (this.getBridge().getHandler())).handleTimeout(this);
    }

    @Override
    public void initialize() {
        super.initialize();
        for (ThingHandler handler : childHandlers)
            handler.initialize();
    }

    @Override
    protected void initializeDevice() {
        super.initializeDevice();
        for (ThingHandler handler : childHandlers)
            handler.initialize();

        if (workFuture != null)
            workFuture.cancel(false);
        if(remoteSwitch != null)
            remoteSwitch.removeSwitchingDoneListener();

        if (this.getDevice() instanceof BrickletRemoteSwitch) {
            remoteSwitch = new BrickletRemoteSwitchWrapper((BrickletRemoteSwitch) this.getDevice());
        } else if (this.getDevice() instanceof BrickletRemoteSwitchV2) {
            remoteSwitch = new BrickletRemoteSwitchV2Wrapper((BrickletRemoteSwitchV2) this.getDevice());
        }
        remoteSwitch.addSwitchingDoneListener(isSwitching);

        try {
            isSwitching.set(remoteSwitch.getSwitchingState() == BrickletRemoteSwitch.SWITCHING_STATE_BUSY);
            workFuture = scheduler.scheduleWithFixedDelay(this::work, 500, 500, TimeUnit.MILLISECONDS);
        } catch (TinkerforgeException e) {
            handleTimeout();
        }
    }

    @Override
    public void handleRemoval() {
        if (workFuture != null)
            workFuture.cancel(true);
        super.handleRemoval();
    }

    public void enqueue(Task task) {
        tasks.add(task);
    }

    private void work() {
        if (isSwitching.get())
            return;

        Task task = tasks.peek();
        if (task == null)
            return;

        isSwitching.set(true);
        tasks.poll(); // Remove peeked task.

        try {
            task.task.accept(remoteSwitch);
        } catch (TinkerforgeException e) {
            task.callback.accept(false);
            this.handleTimeout();
            return;
        }

        task.callback.accept(true);
    }

    // BridgeHandler implementation copied over from BaseBridgeHandler.
    // This should have been an interface with default methods, e.g. a trait.

    /**
     * Finds and returns a child thing for a given UID of this bridge.
     *
     * @param uid uid of the child thing
     * @return child thing with the given uid or null if thing was not found
     */
    public @Nullable Thing getThingByUID(ThingUID uid) {
        Bridge bridge = getThing();

        List<Thing> things = bridge.getThings();

        for (Thing thing : things) {
            if (thing.getUID().equals(uid)) {
                return thing;
            }
        }

        return null;
    }

    @Override
    public Bridge getThing() {
        return (Bridge) super.getThing();
    }

    /**
     * Creates a bridge builder, which allows to modify the bridge. The method
     * {@link BaseThingHandler#updateThing(Thing)} must be called to persist the changes.
     *
     * @return {@link BridgeBuilder} which builds an exact copy of the bridge (not null)
     */
    @Override
    protected BridgeBuilder editThing() {
        return BridgeBuilder.create(this.thing.getThingTypeUID(), this.thing.getUID())
                .withBridge(this.thing.getBridgeUID()).withChannels(this.thing.getChannels())
                .withConfiguration(this.thing.getConfiguration()).withLabel(this.thing.getLabel())
                .withLocation(this.thing.getLocation()).withProperties(this.thing.getProperties());
    }

    @Override
    public void childHandlerInitialized(ThingHandler childHandler, Thing childThing) {
        childHandlers.add(childHandler);
    }

    @Override
    public void childHandlerDisposed(ThingHandler childHandler, Thing childThing) {
        childHandlers.remove(childHandler);
    }
}