const activities = [

    {
        team: "TikTok Agent",
        status: "กำลังสร้างคลิปใหม่",
        color: "bg-green-500",
    },

    {
        team: "Video Agent",
        status: "กำลัง Render วิดีโอ",
        color: "bg-blue-500",
    },

    {
        team: "Developer Agent",
        status: "กำลังเขียนโค้ด",
        color: "bg-purple-500",
    },

    {
        team: "Research Agent",
        status: "กำลังวิเคราะห์คู่แข่ง",
        color: "bg-yellow-500",
    },

    {
        team: "Website Agent",
        status: "กำลัง Deploy เว็บไซต์",
        color: "bg-pink-500",
    },

    {
        team: "Computer Lab",
        status: "Cloud PC Online",
        color: "bg-cyan-500",
    },

    {
        team: "Mobile Lab",
        status: "Android Devices Online",
        color: "bg-orange-500",
    },

];

export default function ActivityFeed() {

    return (

        <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6 h-full">

            <h2 className="text-xl font-bold mb-6">

                Live Activity Feed

            </h2>

            <div className="space-y-4">

                {activities.map((item, index) => (

                    <div
                        key={index}
                        className="flex items-start gap-3 border-b border-zinc-800 pb-4"
                    >

                        <div
                            className={`w-3 h-3 rounded-full mt-2 ${item.color}`}
                        />

                        <div>

                            <h3 className="font-semibold">

                                {item.team}

                            </h3>

                            <p className="text-sm text-zinc-400 mt-1">

                                {item.status}

                            </p>

                        </div>

                    </div>

                ))}

            </div>

        </div>

    );

}
