import DashboardLayout from "../components/DashboardLayout";

export default function SettingsPage() {

    return (

        <DashboardLayout>

            <div className="space-y-8">

                <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-8">

                    <h1 className="text-3xl font-bold text-white">

                        System Settings

                    </h1>

                    <p className="text-zinc-400 mt-2">

                        Configure AI-COMPANY system settings.

                    </p>

                </div>

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">

                    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">

                        <h2 className="text-xl font-bold text-white mb-6">

                            General

                        </h2>

                        <div className="space-y-5">

                            <div>

                                <label className="block text-zinc-400 mb-2">

                                    Company Name

                                </label>

                                <input
                                    className="w-full rounded-xl bg-zinc-950 border border-zinc-700 p-3 text-white"
                                    defaultValue="AI-COMPANY"
                                />

                            </div>

                            <div>

                                <label className="block text-zinc-400 mb-2">

                                    Time Zone

                                </label>

                                <select className="w-full rounded-xl bg-zinc-950 border border-zinc-700 p-3 text-white">

                                    <option>Asia/Bangkok</option>

                                    <option>UTC</option>

                                </select>

                            </div>

                        </div>

                    </div>

                    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">

                        <h2 className="text-xl font-bold text-white mb-6">

                            AI Models

                        </h2>

                        <div className="space-y-4">

                            <button className="w-full rounded-xl bg-cyan-600 hover:bg-cyan-500 py-3">

                                OpenAI

                            </button>

                            <button className="w-full rounded-xl bg-purple-600 hover:bg-purple-500 py-3">

                                Claude

                            </button>

                            <button className="w-full rounded-xl bg-green-600 hover:bg-green-500 py-3">

                                Gemini

                            </button>

                            <button className="w-full rounded-xl bg-orange-600 hover:bg-orange-500 py-3">

                                Local Model

                            </button>

                        </div>

                    </div>

                    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">

                        <h2 className="text-xl font-bold text-white mb-6">

                            Integrations

                        </h2>

                        <div className="space-y-4">

                            <button className="w-full rounded-xl bg-blue-600 py-3">

                                Telegram

                            </button>

                            <button className="w-full rounded-xl bg-gray-700 py-3">

                                GitHub

                            </button>

                            <button className="w-full rounded-xl bg-pink-600 py-3">

                                TikTok

                            </button>

                        </div>

                    </div>

                    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">

                        <h2 className="text-xl font-bold text-white mb-6">

                            System

                        </h2>

                        <div className="space-y-4">

                            <button className="w-full rounded-xl bg-green-600 hover:bg-green-500 py-3">

                                Save Settings

                            </button>

                            <button className="w-full rounded-xl bg-yellow-600 hover:bg-yellow-500 py-3">

                                Restart Services

                            </button>

                            <button className="w-full rounded-xl bg-red-600 hover:bg-red-500 py-3">

                                Shutdown AI Company

                            </button>

                        </div>

                    </div>

                </div>

            </div>

        </DashboardLayout>

    );

}
