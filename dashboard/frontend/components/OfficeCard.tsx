import { useRouter } from "next/router";

interface OfficeCardProps {

    title: string;

    description: string;

    status: string;

    path: string;

}

export default function OfficeCard({

    title,

    description,

    status,

    path,

}: OfficeCardProps) {

    const router = useRouter();

    return (

        <div
            onClick={() => router.push(path)}
            className="cursor-pointer rounded-2xl border border-zinc-800 bg-zinc-900 p-6 hover:border-cyan-500 hover:shadow-xl transition-all duration-300"
        >

            <div className="flex items-center justify-between">

                <h2 className="text-xl font-bold text-white">

                    {title}

                </h2>

                <span className="text-green-400 text-sm">

                    ● {status}

                </span>

            </div>

            <p className="text-zinc-400 mt-4">

                {description}

            </p>

            <div className="mt-6 flex justify-end">

                <button className="px-4 py-2 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white">

                    Open Office

                </button>

            </div>

        </div>

    );

}
