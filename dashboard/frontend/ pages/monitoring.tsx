import DashboardLayout from "../components/DashboardLayout";

export default function MonitoringPage() {

    const services = [

        {
            name: "CEO Service",
            status: "ONLINE",
            uptime: "99.99%",
            cpu: 18,
            memory: 36,
        },

        {
            name: "Manager Service",
            status: "ONLINE",
            uptime: "99.97%",
            cpu: 25,
            memory: 41,
        },

        {
            name: "TikTok Agents",
            status: "ONLINE",
            uptime: "100%",
            cpu: 47,
            memory: 58,
        },

        {
            name: "Video Team",
            status: "ONLINE",
            uptime: "99.95%",
            cpu: 71,
            memory: 74,
        },

        {
            name: "Developer Team",
            status: "ONLINE",
            uptime: "100%",
            cpu: 39,
            memory: 52,
        },

        {
            name: "Research Team",
            status: "ONLINE",
            uptime: "100%",
            cpu: 29,
            memory: 37,
        },

        {
            name: "Website Team",
            status: "ONLINE",
            uptime: "99.98%",
            cpu: 43,
            memory: 48,
        },

        {
            name: "Database",
            status: "ONLINE",
            uptime: "100%",
            cpu: 12,
            memory: 61,
        }

    ];

    return (

        <DashboardLayout>

            <div className="space-y-8">

                <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-8">

                    <h1 className="text-3xl font-bold text-white">

                        System Monitoring

                    </h1>

                    <p className="text-zinc-400 mt-2">

                        Real-time monitoring of all AI services.

                    </p>

                </div>

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">

                    {services.map((service) => (

                        <div
                            key={service.name}
                            className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6"
                        >

                            <div className="flex justify-between">

                                <h2 className="text-xl font-bold text-white">

                                    {service.name}

                                </h2>

                                <span className="text-green-400">

                                    {service.status}

                                </span>

                            </div>

                            <p className="mt-4 text-zinc-400">

                                Uptime

                            </p>

                            <p className="text-white">

                                {service.uptime}

                            </p>

                            <div className="mt-6">

                                <div className="flex justify-between">

                                    <span className="text-zinc-400">

                                        CPU

                                    </span>

                                    <span>

                                        {service.cpu}%

                                    </span>

                                </div>

                                <div className="w-full h-3 rounded-full bg-zinc-800 mt-2">

                                    <div
                                        className="h-3 rounded-full bg-cyan-500"
                                        style={{ width: `${service.cpu}%` }}
                                    />

                                </div>

                            </div>

                            <div className="mt-6">

                                <div className="flex justify-between">

                                    <span className="text-zinc-400">

                                        Memory

                                    </span>

                                    <span>

                                        {service.memory}%

                                    </span>

                                </div>

                                <div className="w-full h-3 rounded-full bg-zinc-800 mt-2">

                                    <div
                                        className="h-3 rounded-full bg-green-500"
                                        style={{ width: `${service.memory}%` }}
                                    />

                                </div>

                            </div>

                        </div>

                    ))}

                </div>

            </div>

        </DashboardLayout>

    );

}
