interface AgentCardProps {

    name: string;

    role: string;

    status: string;

    currentTask: string;

    progress: number;

}

export default function AgentCard({

    name,

    role,

    status,

    currentTask,

    progress,

}: AgentCardProps) {

    return (

        <div className="rounded-2xl border border-zinc-800 bg-zinc-900 p-6 hover:border-cyan-500 transition-all duration-300">

            <div className="flex items-center justify-between">

                <div>

                    <h2 className="text-lg font-bold text-white">

                        {name}

                    </h2>

                    <p className="text-zinc-400 text-sm mt-1">

                        {role}

                    </p>

                </div>

                <span
                    className={`text-sm font-semibold ${
                        status === "ONLINE"
                            ? "text-green-400"
                            : "text-red-400"
                    }`}
                >

                    ● {status}

                </span>

            </div>

            <div className="mt-6">

                <p className="text-zinc-400 text-sm">

                    Current Task

                </p>

                <p className="text-white mt-2">

                    {currentTask}

                </p>

            </div>

            <div className="mt-6">

                <div className="flex justify-between mb-2">

                    <span className="text-zinc-400">

                        Progress

                    </span>

                    <span className="text-cyan-400">

                        {progress}%

                    </span>

                </div>

                <div className="w-full h-2 rounded-full bg-zinc-800">

                    <div
                        className="h-2 rounded-full bg-cyan-500"
                        style={{ width: `${progress}%` }}
                    />

                </div>

            </div>

        </div>

    );

}
