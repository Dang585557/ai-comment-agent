import DashboardLayout from "../components/DashboardLayout";

export default function MobileLabPage() {

    const devices = [

        {
            id: "ANDROID-01",
            platform: "Android",
            status: "ONLINE",
            task: "TikTok Live",
            battery: 92,
        },

        {
            id: "ANDROID-02",
            platform: "Android",
            status: "ONLINE",
            task: "TikTok Shop",
            battery: 84,
        },

        {
            id: "ANDROID-03",
            platform: "Android",
            status: "ONLINE",
            task: "Testing",
            battery: 71,
        },

        {
            id: "IOS-01",
            platform: "iPhone",
            status: "ONLINE",
            task: "QA Testing",
            battery: 88,
        },

        {
            id: "IOS-02",
            platform: "iPhone",
            status: "OFFLINE",
            task: "Charging",
            battery: 21,
        },

        {
            id: "ANDROID-04",
            platform: "Android",
            status: "ONLINE",
            task: "Automation",
            battery: 97,
        }

    ];

    return (

        <DashboardLayout>

            <div className="space-y-8">

                <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-8">

                    <h1 className="text-3xl font-bold text-white">

                        Mobile Lab

                    </h1>

                    <p className="text-zinc-400 mt-2">

                        Monitor all Android and iPhone devices.

                    </p>

                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">

                    {devices.map((device) => (

                        <div
                            key={device.id}
                            className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6"
                        >

                            <div className="flex justify-between items-center">

                                <h2 className="text-lg font-bold text-white">

                                    {device.id}

                                </h2>

                                <span
                                    className={
                                        device.status === "ONLINE"
                                            ? "text-green-400"
                                            : "text-red-400"
                                    }
                                >
                                    {device.status}
                                </span>

                            </div>

                            <p className="mt-4 text-zinc-500">

                                Platform

                            </p>

                            <p className="text-white">

                                {device.platform}

                            </p>

                            <p className="mt-4 text-zinc-500">

                                Current Task

                            </p>

                            <p className="text-white">

                                {device.task}

                            </p>

                            <div className="mt-6">

                                <div className="flex justify-between text-sm">

                                    <span className="text-zinc-400">

                                        Battery

                                    </span>

                                    <span className="text-white">

                                        {device.battery}%

                                    </span>

                                </div>

                                <div className="w-full bg-zinc-800 rounded-full h-3 mt-2">

                                    <div
                                        className="bg-green-500 h-3 rounded-full"
                                        style={{
                                            width: `${device.battery}%`
                                        }}
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
