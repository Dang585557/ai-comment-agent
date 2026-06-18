import DashboardLayout from "../components/DashboardLayout";

export default function StoragePage() {

    const storage = [

        {
            name: "Videos",
            used: "324 GB",
            total: "1 TB",
            progress: 32,
        },

        {
            name: "Images",
            used: "118 GB",
            total: "500 GB",
            progress: 24,
        },

        {
            name: "Audio",
            used: "46 GB",
            total: "200 GB",
            progress: 23,
        },

        {
            name: "Scripts",
            used: "5 GB",
            total: "100 GB",
            progress: 5,
        },

        {
            name: "Reports",
            used: "18 GB",
            total: "100 GB",
            progress: 18,
        },

        {
            name: "Backups",
            used: "690 GB",
            total: "2 TB",
            progress: 34,
        },

        {
            name: "Exports",
            used: "41 GB",
            total: "300 GB",
            progress: 14,
        }

    ];

    return (

        <DashboardLayout>

            <div className="space-y-8">

                <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-8">

                    <h1 className="text-3xl font-bold text-white">

                        Storage Center

                    </h1>

                    <p className="text-zinc-400 mt-2">

                        Monitor storage usage across AI-COMPANY.

                    </p>

                </div>

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">

                    {storage.map((item) => (

                        <div
                            key={item.name}
                            className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6"
                        >

                            <div className="flex justify-between items-center">

                                <h2 className="text-xl font-bold text-white">

                                    {item.name}

                                </h2>

                                <span className="text-zinc-400">

                                    {item.used} / {item.total}

                                </span>

                            </div>

                            <div className="mt-6">

                                <div className="flex justify-between text-sm">

                                    <span className="text-zinc-400">

                                        Usage

                                    </span>

                                    <span className="text-white">

                                        {item.progress}%

                                    </span>

                                </div>

                                <div className="w-full h-3 bg-zinc-800 rounded-full mt-2">

                                    <div
                                        className="h-3 bg-cyan-500 rounded-full"
                                        style={{
                                            width: `${item.progress}%`
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
