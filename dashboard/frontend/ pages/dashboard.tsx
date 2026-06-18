import DashboardLayout from "../components/DashboardLayout";
import SummaryCards from "../components/SummaryCards";
import OfficeOverview from "../components/OfficeOverview";
import ActivityFeed from "../components/ActivityFeed";
import RecentTasks from "../components/RecentTasks";
import QuickActions from "../components/QuickActions";

export default function DashboardPage() {

    return (

        <DashboardLayout>

            <div className="grid grid-cols-12 gap-6">

                <div className="col-span-9 space-y-6">

                    <SummaryCards />

                    <OfficeOverview />

                    <RecentTasks />

                    <QuickActions />

                </div>

                <div className="col-span-3">

                    <ActivityFeed />

                </div>

            </div>

        </DashboardLayout>

    );

}
