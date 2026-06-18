import { useRouter } from "next/router";

const offices = [

    {
        title: "CEO Office",
        path: "/ceo",
        status: "Online"
    },

    {
        title: "AI Manager Office",
        path: "/manager",
        status: "Online"
    },

    {
        title: "TikTok Team",
        path: "/teams/tiktok",
        status: "Working"
    },

    {
        title: "Video Editing Team",
        path: "/teams/video",
        status: "Rendering"
    },

    {
        title: "Developer Team",
        path: "/teams/developer",
        status: "Coding"
    },

    {
        title: "Research Team",
        path: "/teams/research",
        status: "Analyzing"
    },

    {
        title: "Website Team",
        path: "/teams/website",
        status: "Deploying"
    },

    {
        title: "Computer Lab",
        path: "/computer-lab",
        status: "5 PCs Online"
    },

    {
        title: "Mobile Lab",
        path: "/mobile-lab",
        status: "12 Devices"
    }

];

export default function OfficeOverview() {

    const router = useRouter();

    return (

        <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">

            <h2 className="text-2xl font-bold mb-6">

                Office Overview

            </h2>

            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5">

                {offices.map((office) => (

                    <div

                        key={office.title}

                        onClick={() => router.push(office.path)}

                        className="cursor-pointer rounded-xl border border-zinc-700 bg-zinc-950 p-5 hover:border-cyan-500 hover:scale-105 transition-all"

                    >

                        <h3 className="text-lg font-bold">

                            {office.title}

                        </h3>

                        <p className="text-green-400 mt-3">

                            ● {office.status}

                        </p>

                        <div className="mt-6 text-sm text-zinc-400">

                            Click to Open Office

                        </div>

                    </div>

                ))}

            </div>

        </div>

    );

}
