const logs = [

    {
        time: "10:15:22",
        level: "INFO",
        message: "AI-COMPANY Started",
    },

    {
        time: "10:16:08",
        level: "SUCCESS",
        message: "TikTok Agent Connected",
    },

    {
        time: "10:17:31",
        level: "INFO",
        message: "Developer Agent Running",
    },

    {
        time: "10:18:42",
        level: "WARNING",
        message: "Video Queue Increasing",
    },

    {
        time: "10:19:55",
        level: "SUCCESS",
        message: "Website Deploy Complete",
    },

];

export default function LogViewer() {

    return (

        <div className="rounded-2xl bg-zinc-900 border border-zinc-800 p-6">

            <h2 className="text-xl font-bold text-white mb-6">

                System Logs

            </h2>

            <div className="space-y-4 max-h-[500px] overflow-y-auto">

                {logs.map((log, index) => (

                    <div
                        key={index}
                        className="border-b border-zinc-800 pb-3"
                    >

                        <div className="flex justify-between">

                            <span className="text-cyan-400">

                                {log.time}

                            </span>

                            <span className="text-zinc-400">

                                {log.level}

                            </span>

                        </div>

                        <p className="text-white mt-2">

                            {log.message}

                        </p>

                    </div>

                ))}

            </div>

        </div>

    );

}
