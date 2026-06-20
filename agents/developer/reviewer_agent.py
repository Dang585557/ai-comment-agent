from datetime import datetime


class ReviewerAgent:

    def review(
        self,
        filename: str,
        code: str
    ):

        issues = []

        if "TODO" in code:
            issues.append("Found TODO comments.")

        if len(code.splitlines()) > 500:
            issues.append("Large file. Consider splitting modules.")

        return {
            "filename": filename,
            "passed": len(issues) == 0,
            "issues": issues,
            "reviewed_at": datetime.now().isoformat()
        }

    def score(self, review_result: dict):

        if review_result["passed"]:
            return 100

        score = 100 - (len(review_result["issues"]) * 10)

        return max(score, 0)

    def summary(self, review_result: dict):

        return {
            "filename": review_result["filename"],
            "score": self.score(review_result),
            "passed": review_result["passed"],
            "total_issues": len(review_result["issues"])
        }


if __name__ == "__main__":

    agent = ReviewerAgent()

    result = agent.review(
        "main.py",
        "print('Hello AI-COMPANY')"
    )

    print(agent.summary(result))
