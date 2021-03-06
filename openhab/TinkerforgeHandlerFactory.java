/**
 * Copyright (c) 2010-2020 Contributors to the openHAB project
 *
 * See the NOTICE file(s) distributed with this work for additional
 * information.
 *
 * This program and the accompanying materials are made available under the
 * terms of the Eclipse Public License 2.0 which is available at
 * http://www.eclipse.org/legal/epl-2.0
 *
 * SPDX-License-Identifier: EPL-2.0
 */
package org.openhab.binding.tinkerforge.internal;

import static org.openhab.binding.tinkerforge.internal.TinkerforgeBindingConstants.THING_TYPE_BRICKLET_OUTDOOR_WEATHER;
import static org.openhab.binding.tinkerforge.internal.TinkerforgeBindingConstants.THING_TYPE_BRICKLET_REMOTE_SWITCH;
import static org.openhab.binding.tinkerforge.internal.TinkerforgeBindingConstants.THING_TYPE_BRICKLET_REMOTE_SWITCH_V2;
import static org.openhab.binding.tinkerforge.internal.TinkerforgeBindingConstants.THING_TYPE_BRICK_DAEMON;
import static org.openhab.binding.tinkerforge.internal.TinkerforgeBindingConstants.THING_TYPE_OUTDOOR_WEATHER_SENSOR;
import static org.openhab.binding.tinkerforge.internal.TinkerforgeBindingConstants.THING_TYPE_OUTDOOR_WEATHER_STATION;
import static org.openhab.binding.tinkerforge.internal.TinkerforgeBindingConstants.THING_TYPE_REMOTE_DIMMER_TYPE_B;
import static org.openhab.binding.tinkerforge.internal.TinkerforgeBindingConstants.THING_TYPE_REMOTE_SOCKET_TYPE_A;
import static org.openhab.binding.tinkerforge.internal.TinkerforgeBindingConstants.THING_TYPE_REMOTE_SOCKET_TYPE_B;
import static org.openhab.binding.tinkerforge.internal.TinkerforgeBindingConstants.THING_TYPE_REMOTE_SOCKET_TYPE_C;

import java.util.HashMap;
import java.util.Hashtable;
import java.util.Map;
import java.util.function.Supplier;

import org.eclipse.jdt.annotation.NonNullByDefault;
import org.eclipse.jdt.annotation.Nullable;
import org.eclipse.jetty.client.HttpClient;
import org.openhab.binding.tinkerforge.discovery.BrickDaemonDiscoveryService;
import org.openhab.binding.tinkerforge.internal.device.DeviceWrapper;
import org.openhab.binding.tinkerforge.internal.device.DeviceWrapperFactory;
import org.openhab.binding.tinkerforge.internal.device.RemoteDimmerTypeB;
import org.openhab.binding.tinkerforge.internal.device.RemoteSocketTypeA;
import org.openhab.binding.tinkerforge.internal.device.RemoteSocketTypeB;
import org.openhab.binding.tinkerforge.internal.device.RemoteSocketTypeC;
import org.openhab.binding.tinkerforge.internal.handler.BrickDaemonHandler;
import org.openhab.binding.tinkerforge.internal.handler.BrickletOutdoorWeatherHandler;
import org.openhab.binding.tinkerforge.internal.handler.BrickletOutdoorWeatherSensorHandler;
import org.openhab.binding.tinkerforge.internal.handler.BrickletOutdoorWeatherStationHandler;
import org.openhab.binding.tinkerforge.internal.handler.BrickletRemoteSwitchHandler;
import org.openhab.binding.tinkerforge.internal.handler.DeviceHandler;
import org.openhab.binding.tinkerforge.internal.handler.RemoteSwitchDeviceHandler;
import org.eclipse.smarthome.config.core.ConfigDescriptionRegistry;
import org.eclipse.smarthome.config.discovery.DiscoveryService;
import org.eclipse.smarthome.core.thing.Bridge;
import org.eclipse.smarthome.core.thing.Thing;
import org.eclipse.smarthome.core.thing.ThingTypeUID;
import org.eclipse.smarthome.core.thing.binding.BaseThingHandlerFactory;
import org.eclipse.smarthome.core.thing.binding.ThingHandler;
import org.eclipse.smarthome.core.thing.binding.ThingHandlerFactory;
import org.eclipse.smarthome.core.thing.type.ChannelTypeRegistry;
import org.eclipse.smarthome.io.net.http.HttpClientFactory;
import org.osgi.framework.ServiceRegistration;
import org.osgi.service.component.annotations.Component;
import org.osgi.service.component.annotations.Reference;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.tinkerforge.IPConnection;

/**
 * The {@link TinkerforgeHandlerFactory} is responsible for creating things and
 * thing handlers.
 *
 * @author Erik Fleckstein - Initial contribution
 */
@NonNullByDefault
@Component(configurationPid = "binding.tinkerforge", service = ThingHandlerFactory.class)
public class TinkerforgeHandlerFactory extends BaseThingHandlerFactory {
    private final Map<BrickDaemonDiscoveryService, @Nullable ServiceRegistration<?>> discoveryServiceRegs = new HashMap<>();

    private final Logger logger = LoggerFactory.getLogger(TinkerforgeHandlerFactory.class);
    private @Nullable HttpClient httpClient;

    @Override
    public boolean supportsThingType(ThingTypeUID thingTypeUID) {
        return TinkerforgeBindingConstants.SUPPORTED_DEVICES.contains(thingTypeUID);
    }

    private DeviceWrapper createDevice(String thingName, String uid, IPConnection ipcon) {
        try {
            return DeviceWrapperFactory.createDevice(thingName, uid, ipcon);
        } catch (Exception e) {
            logger.error("Failed to create device {} (uid {}):", thingName, uid, e);
            throw new AssertionError("Failed to create device %s (uid %s).", e);
        }
    }

    @Override
    protected @Nullable ThingHandler createHandler(Thing thing) {
        ThingTypeUID thingTypeUID = thing.getThingTypeUID();
        String thingName = thingTypeUID.getId();

        Supplier<ChannelTypeRegistry> ctRegSupplier = () -> this.bundleContext
                .getService(this.bundleContext.getServiceReference(ChannelTypeRegistry.class));

        Supplier<ConfigDescriptionRegistry> confDescRegSupplier = () -> this.bundleContext
                .getService(this.bundleContext.getServiceReference(ConfigDescriptionRegistry.class));

        if (thingTypeUID.equals(THING_TYPE_BRICK_DAEMON)) {
            assert (thing instanceof Bridge);
            return new BrickDaemonHandler((Bridge) thing, this::registerBrickDaemonDiscoveryService,
                    this::deregisterBrickDaemonDiscoveryService);
        } else if (thingTypeUID.equals(THING_TYPE_BRICKLET_OUTDOOR_WEATHER)) {
            assert (thing instanceof Bridge);
            return new BrickletOutdoorWeatherHandler((Bridge) thing,
                    (String uid, IPConnection ipcon) -> createDevice(thingTypeUID.getId(), uid, ipcon),
                    DeviceWrapperFactory.getDeviceInfo(thingName).deviceActionsClass, ctRegSupplier,
                    confDescRegSupplier, httpClient);
        } else if (thingTypeUID.equals(THING_TYPE_BRICKLET_REMOTE_SWITCH)
                || thingTypeUID.equals(THING_TYPE_BRICKLET_REMOTE_SWITCH_V2)) {
            assert (thing instanceof Bridge);
            return new BrickletRemoteSwitchHandler((Bridge) thing,
                    (String uid, IPConnection ipcon) -> createDevice(thingTypeUID.getId(), uid, ipcon),
                    DeviceWrapperFactory.getDeviceInfo(thingName).deviceActionsClass, ctRegSupplier,
                    confDescRegSupplier, httpClient);
        } else if (thingTypeUID.equals(THING_TYPE_OUTDOOR_WEATHER_STATION)) {
            return new BrickletOutdoorWeatherStationHandler(thing, ctRegSupplier, confDescRegSupplier);
        } else if (thingTypeUID.equals(THING_TYPE_OUTDOOR_WEATHER_SENSOR)) {
            return new BrickletOutdoorWeatherSensorHandler(thing, ctRegSupplier, confDescRegSupplier);
        } else if (thingTypeUID.equals(THING_TYPE_REMOTE_SOCKET_TYPE_A)) {
            return new RemoteSwitchDeviceHandler(thing, (handler) -> new RemoteSocketTypeA(handler), ctRegSupplier, confDescRegSupplier);
        } else if (thingTypeUID.equals(THING_TYPE_REMOTE_SOCKET_TYPE_B)) {
            return new RemoteSwitchDeviceHandler(thing, (handler) -> new RemoteSocketTypeB(handler), ctRegSupplier, confDescRegSupplier);
        } else if (thingTypeUID.equals(THING_TYPE_REMOTE_SOCKET_TYPE_C)) {
            return new RemoteSwitchDeviceHandler(thing, (handler) -> new RemoteSocketTypeC(handler), ctRegSupplier, confDescRegSupplier);
        } else if (thingTypeUID.equals(THING_TYPE_REMOTE_DIMMER_TYPE_B)) {
            return new RemoteSwitchDeviceHandler(thing, (handler) -> new RemoteDimmerTypeB(handler), ctRegSupplier, confDescRegSupplier);
        }

        return new DeviceHandler(thing, (String uid, IPConnection ipcon) -> createDevice(thingName, uid, ipcon),
                DeviceWrapperFactory.getDeviceInfo(thingName).deviceActionsClass,
                () -> this.bundleContext.getService(this.bundleContext.getServiceReference(ChannelTypeRegistry.class)),
                () -> this.bundleContext
                        .getService(this.bundleContext.getServiceReference(ConfigDescriptionRegistry.class)),
                httpClient);
    }

    private synchronized void registerBrickDaemonDiscoveryService(BrickDaemonDiscoveryService service) {
        this.discoveryServiceRegs.put(service, bundleContext.registerService(DiscoveryService.class.getName(), service,
                new Hashtable<String, Object>()));
    }

    private synchronized void deregisterBrickDaemonDiscoveryService(BrickDaemonDiscoveryService service) {
        ServiceRegistration<?> serviceReg = this.discoveryServiceRegs.remove(service);
        if (serviceReg != null) {
            // remove discovery service, if bridge handler is removed
            serviceReg.unregister();
            service.stopDiscovery();
        }
    }

    @Reference
    protected void setHttpClientFactory(HttpClientFactory httpClientFactory) {
        this.httpClient = httpClientFactory.getCommonHttpClient();
    }

    protected void unsetHttpClientFactory(HttpClientFactory httpClientFactory) {
        this.httpClient = null;
    }
}
