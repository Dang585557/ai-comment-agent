import DashboardLayout from "../components/DashboardLayout";

export default function CEOOffice() {

    return (

        <DashboardLayout>

            <div className="space-y-6">

                <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-8">

                    <h1 className="text-3xl font-bold text-white">

                        CEO Office

                    </h1>

                    <p className="text-zinc-400 mt-3">

                        Command the entire AI Company from here.

                    </p>

                </div>

                <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

                    <div className="lg:col-span-2 bg-zinc-900 border border-zinc-800 rounded-2xl p-6">

                        <h2 className="text-xl font-bold text-white mb-4">

                            Command Console

                        </h2>

                        <textarea
                            className="w-full h-48 rounded-xl bg-zinc-950 border border-zinc-700 p-4 text-white"
                            placeholder="Type command for AI Manager..."
                        />

                        <div className="mt-6 flex gap-4">

                            <button className="px-6 py-3 rounded-xl bg-cyan-600 hover:bg-cyan-500">

                                Send Command

                            </button>

                            <button className="px-6 py-3 rounded-xl bg-green-600 hover:bg-green-500">

                                Generate Report

                            </button>

                            <button className="px-6 py-3 rounded-xl bg-red-600 hover:bg-red-500">

                                Emergency Stop

                            </button>

                        </div>

                    </div>

                    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">

                        <h2 className="text-xl font-bold text-white mb-4">

                            CEO Status

                        </h2>

                        <div className="space-y-4">

                            <div className="flex justify-between">

                                <span>AI Manager</span>

                                <span className="text-green-400">

                                    ● Online

                                </span>

                            </div>

                            <div className="flex justify-between">

                                <span>Teams</span>

                                <span>5 Active</span>

                            </div>

                            <div className="flex justify-between">

                                <span>Tasks</span>

                                <span>12 Running</span>

                            </div>

                            <div className="flex justify-between">

                                <span>Cloud PCs</span>

                                <span>4 Online</span>

                            </div>

                            <div className="flex justify-between">

                                <span>Mobile Devices</span>

                                <span>8 Online</span>

                            </div>

                        </div>

                    </div>

                </div>

            </div>

        </DashboardLayout>

    );

}
