import DashboardLayout from "../components/DashboardLayout";

export default function ManagerPage() {

    return (

        <DashboardLayout>

            <div className="space-y-6">

                <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-8">

                    <h1 className="text-3xl font-bold text-white">

                        AI Manager Office

                    </h1>

                    <p className="text-zinc-400 mt-3">

                        Monitor, assign and coordinate every AI team.

                    </p>

                </div>

                <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">

                    <div className="xl:col-span-2 bg-zinc-900 border border-zinc-800 rounded-2xl p-6">

                        <h2 className="text-xl font-bold mb-6">

                            Team Overview

                        </h2>

                        <div className="space-y-4">

                            {[
                                {
                                    name: "TikTok Team",
                                    status: "Working",
                                    progress: 75,
                                },
                                {
                                    name: "Video Team",
                                    status: "Rendering",
                                    progress: 62,
                                },
                                {
                                    name: "Developer Team",
                                    status: "Coding",
                                    progress: 48,
                                },
                                {
                                    name: "Research Team",
                                    status: "Analyzing",
                                    progress: 91,
                                },
                                {
                                    name: "Website Team",
                                    status: "Deploying",
                                    progress: 35,
                                },
                            ].map((team) => (

                                <div
                                    key={team.name}
                                    className="rounded-xl border border-zinc-800 bg-zinc-950 p-5"
                                >

                                    <div className="flex justify-between">

                                        <h3 className="font-bold">

                                            {team.name}

                                        </h3>

                                        <span className="text-green-400">

                                            {team.status}

                                        </span>

                                    </div>

                                    <div className="mt-4 w-full bg-zinc-800 rounded-full h-3">

                                        <div
                                            className="bg-cyan-500 h-3 rounded-full"
                                            style={{
                                                width: `${team.progress}%`
                                            }}
                                        />

                                    </div>

                                    <div className="mt-2 text-sm text-zinc-400">

                                        {team.progress}% Completed

                                    </div>

                                </div>

                            ))}

                        </div>

                    </div>

                    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">

                        <h2 className="text-xl font-bold mb-6">

                            Manager Panel

                        </h2>

                        <div className="space-y-4">

                            <button className="w-full bg-cyan-600 hover:bg-cyan-500 rounded-xl py-3">

                                Assign Tasks

                            </button>

                            <button className="w-full bg-green-600 hover:bg-green-500 rounded-xl py-3">

                                Create Team

                            </button>

                            <button className="w-full bg-purple-600 hover:bg-purple-500 rounded-xl py-3">

                                View Reports

                            </button>

                            <button className="w-full bg-orange-600 hover:bg-orange-500 rounded-xl py-3">

                                Team Analytics

                            </button>

                            <button className="w-full bg-red-600 hover:bg-red-500 rounded-xl py-3">

                                Stop All Tasks

                            </button>

                        </div>

                    </div>

                </div>

            </div>

        </DashboardLayout>

    );

}
