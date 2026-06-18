import { useEffect, useState } from "react";

export default function SystemStatus() {

    const [status, setStatus] = useState({
        online: true,
        cpu: 12,
        ram: 34,
        storage: 48,
        agents: 25,
        tasks: 8,
    });

    useEffect(() => {

        const timer = setInterval(() => {

            setStatus((prev) => ({

                ...prev,

                cpu: Math.floor(Math.random() * 30) + 10,

                ram: Math.floor(Math.random() * 40) + 20,

                tasks: Math.floor(Math.random() * 20) + 1,

            }));

        }, 3000);

        return () => clearInterval(timer);

    }, []);

    return (

        <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">

            <h2 className="text-xl font-bold text-white mb-6">

                System Status

            </h2>

            <div className="space-y-5">

                <div className="flex justify-between">

                    <span className="text-zinc-400">

                        System

                    </span>

                    <span className="text-green-400">

                        ● ONLINE

                    </span>

                </div>

                <div>

                    <div className="flex justify-between mb-2">

                        <span>CPU</span>

                        <span>{status.cpu}%</span>

                    </div>

                    <div className="w-full bg-zinc-800 rounded-full h-2">

                        <div
                            className="bg-cyan-500 h-2 rounded-full"
                            style={{ width: `${status.cpu}%` }}
                        />

                    </div>

                </div>

                <div>

                    <div className="flex justify-between mb-2">

                        <span>RAM</span>

                        <span>{status.ram}%</span>

                    </div>

                    <div className="w-full bg-zinc-800 rounded-full h-2">

                        <div
                            className="bg-green-500 h-2 rounded-full"
                            style={{ width: `${status.ram}%` }}
                        />

                    </div>

                </div>

                <div>

                    <div className="flex justify-between mb-2">

                        <span>Storage</span>

                        <span>{status.storage}%</span>

                    </div>

                    <div className="w-full bg-zinc-800 rounded-full h-2">

                        <div
                            className="bg-purple-500 h-2 rounded-full"
                            style={{ width: `${status.storage}%` }}
                        />

                    </div>

                </div>

                <div className="grid grid-cols-2 gap-4 pt-4">

                    <div className="bg-zinc-800 rounded-xl p-4">

                        <p className="text-zinc-400 text-sm">

                            Agents

                        </p>

                        <p className="text-2xl font-bold text-cyan-400">

                            {status.agents}

                        </p>

                    </div>

                    <div className="bg-zinc-800 rounded-xl p-4">

                        <p className="text-zinc-400 text-sm">

                            Tasks

                        </p>

                        <p className="text-2xl font-bold text-green-400">

                            {status.tasks}

                        </p>

                    </div>

                </div>

            </div>

        </div>

    );

}
