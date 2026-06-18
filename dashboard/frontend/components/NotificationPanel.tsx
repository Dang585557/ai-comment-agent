const notifications = [

    {
        title: "New Task",
        message: "TikTok Team received a new task.",
        time: "1 min ago",
        type: "info",
    },

    {
        title: "Render Complete",
        message: "Video Team finished rendering.",
        time: "3 mins ago",
        type: "success",
    },

    {
        title: "Code Updated",
        message: "Developer Team pushed new commit.",
        time: "8 mins ago",
        type: "success",
    },

    {
        title: "High CPU Usage",
        message: "Computer Lab CPU usage exceeded 80%.",
        time: "12 mins ago",
        type: "warning",
    },

    {
        title: "Deployment Complete",
        message: "Website deployed successfully.",
        time: "20 mins ago",
        type: "success",
    }

];

export default function NotificationPanel() {

    return (

        <div className="rounded-2xl border border-zinc-800 bg-zinc-900 p-6">

            <h2 className="text-xl font-bold text-white mb-6">

                Notifications

            </h2>

            <div className="space-y-4">

                {notifications.map((item, index) => (

                    <div
                        key={index}
                        className="rounded-xl border border-zinc-800 bg-zinc-950 p-4"
                    >

                        <div className="flex justify-between items-center">

                            <h3 className="font-semibold text-white">

                                {item.title}

                            </h3>

                            <span className="text-xs text-zinc-500">

                                {item.time}

                            </span>

                        </div>

                        <p className="text-zinc-400 text-sm mt-2">

                            {item.message}

                        </p>

                    </div>

                ))}

            </div>

        </div>

    );

}
