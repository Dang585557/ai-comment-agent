import { useRouter } from "next/router";

interface TeamCardProps {

    name: string;

    description: string;

    members: number;

    status: string;

    path: string;

}

export default function TeamCard({

    name,

    description,

    members,

    status,

    path,

}: TeamCardProps) {

    const router = useRouter();

    return (

        <div
            onClick={() => router.push(path)}
            className="cursor-pointer rounded-2xl bg-zinc-900 border border-zinc-800 p-6 hover:border-cyan-500 transition-all duration-300"
        >

            <div className="flex items-center justify-between">

                <h2 className="text-xl font-bold text-white">

                    {name}

                </h2>

                <span className="text-green-400">

                    ● {status}

                </span>

            </div>

            <p className="text-zinc-400 mt-4">

                {description}

            </p>

            <div className="mt-6 flex items-center justify-between">

                <div>

                    <p className="text-sm text-zinc-500">

                        Members

                    </p>

                    <p className="text-2xl font-bold text-cyan-400">

                        {members}

                    </p>

                </div>

                <button className="px-4 py-2 rounded-lg bg-cyan-600 hover:bg-cyan-500">

                    Open Team

                </button>

            </div>

        </div>

    );

}
