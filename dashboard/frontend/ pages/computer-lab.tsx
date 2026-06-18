import DashboardLayout from "../components/DashboardLayout";

export default function ComputerLabPage() {

    const computers = [

        {
            id: "PC-01",
            status: "ONLINE",
            task: "TikTok Browser",
            cpu: 34,
            ram: 48,
        },

        {
            id: "PC-02",
            status: "ONLINE",
            task: "Video Rendering",
            cpu: 82,
            ram: 76,
        },

        {
            id: "PC-03",
            status: "ONLINE",
            task: "AI Coding",
            cpu: 55,
            ram: 63,
        },

        {
            id: "PC-04",
            status: "ONLINE",
            task: "Research",
            cpu: 29,
            ram: 41,
        },

        {
            id: "PC-05",
            status: "OFFLINE",
            task: "Idle",
            cpu: 0,
            ram: 0,
        },

        {
            id: "PC-06",
            status: "ONLINE",
            task: "Dashboard Server",
            cpu: 47,
            ram: 58,
        }

    ];

    return (

        <DashboardLayout>

            <div className="space-y-8">

                <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-8">

                    <h1 className="text-3xl font-bold text-white">

                        Computer Lab

                    </h1>

                    <p className="text-zinc-400 mt-2">

                        Monitor every computer inside AI-COMPANY.

                    </p>

                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">

                    {computers.map((pc) => (

                        <div
                            key={pc.id}
                            className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6"
                        >

                            <div className="flex justify-between">

                                <h2 className="text-xl font-bold">

                                    {pc.id}

                                </h2>

                                <span className={pc.status === "ONLINE"
                                    ? "text-green-400"
                                    : "text-red-400"}>

                                    {pc.status}

                                </span>

                            </div>

                            <p className="mt-4 text-zinc-400">

                                Task

                            </p>

                            <p className="font-semibold">

                                {pc.task}

                            </p>

                            <div className="mt-6">

                                <p className="text-sm text-zinc-400">

                                    CPU {pc.cpu}%

                                </p>

                                <div className="w-full bg-zinc-800 h-3 rounded-full mt-2">

                                    <div
                                        className="bg-cyan-500 h-3 rounded-full"
                                        style={{ width: `${pc.cpu}%` }}
                                    />

                                </div>

                            </div>

                            <div className="mt-6">

                                <p className="text-sm text-zinc-400">

                                    RAM {pc.ram}%

                                </p>

                                <div className="w-full bg-zinc-800 h-3 rounded-full mt-2">

                                    <div
                                        className="bg-green-500 h-3 rounded-full"
                                        style={{ width: `${pc.ram}%` }}
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
