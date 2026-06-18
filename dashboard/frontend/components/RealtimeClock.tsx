import { useEffect, useState } from "react";

export default function RealtimeClock() {

    const [time, setTime] = useState("");

    useEffect(() => {

        const updateTime = () => {

            setTime(
                new Date().toLocaleString()
            );

        };

        updateTime();

        const interval = setInterval(updateTime, 1000);

        return () => clearInterval(interval);

    }, []);

    return (

        <div className="rounded-2xl bg-zinc-900 border border-zinc-800 p-6">

            <h2 className="text-xl font-bold text-white mb-4">

                Realtime Clock

            </h2>

            <div className="text-center">

                <p className="text-4xl font-bold text-cyan-400">

                    {new Date().toLocaleTimeString()}

                </p>

                <p className="mt-3 text-zinc-400">

                    {time}

                </p>

                <div className="mt-6 flex justify-center items-center gap-2">

                    <div className="w-3 h-3 rounded-full bg-green-500 animate-pulse"></div>

                    <span className="text-green-400">

                        System Running

                    </span>

                </div>

            </div>

        </div>

    );

}
