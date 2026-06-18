import { useEffect, useState } from "react";

export default function Header() {

    const [currentTime, setCurrentTime] = useState("");

    useEffect(() => {

        const timer = setInterval(() => {

            setCurrentTime(
                new Date().toLocaleString()
            );

        }, 1000);

        return () => clearInterval(timer);

    }, []);

    return (

        <header className="h-20 bg-zinc-900 border-b border-zinc-800 flex items-center justify-between px-8">

            <div>

                <h1 className="text-2xl font-bold text-white">

                    AI Company Dashboard

                </h1>

                <div className="flex items-center gap-2 mt-2">

                    <div className="w-3 h-3 rounded-full bg-green-500 animate-pulse" />

                    <span className="text-green-400">

                        System Online

                    </span>

                </div>

            </div>

            <div className="flex items-center gap-8">

                <div className="text-right">

                    <p className="text-zinc-400 text-sm">

                        Current Time

                    </p>

                    <p className="text-white font-semibold">

                        {currentTime}

                    </p>

                </div>

                <div className="flex items-center gap-4">

                    <div className="w-12 h-12 rounded-full bg-cyan-600 flex items-center justify-center text-white font-bold">

                        CEO

                    </div>

                    <div>

                        <p className="text-white font-semibold">

                            CEO

                        </p>

                        <p className="text-zinc-400 text-sm">

                            Administrator

                        </p>

                    </div>

                </div>

            </div>

        </header>

    );

}
