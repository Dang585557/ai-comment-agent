from datetime import datetime


class SEOAgent:

    def analyze(
        self,
        title: str,
        description: str,
        keywords: list
    ):

        score = min(100, 70 + len(keywords) * 3)

        return {
            "title": title,
            "description_length": len(description),
            "keywords": keywords,
            "seo_score": score,
            "status": "ANALYZED",
            "generated_at": datetime.now().isoformat()
        }

    def recommendations(self):

        return [
            "Use a descriptive page title.",
            "Include primary keywords in the title.",
            "Write a meta description between 120-160 characters.",
            "Optimize image alt text.",
            "Improve page loading speed."
        ]

    def report(
        self,
        analysis: dict
    ):

        return {
            "score": analysis["seo_score"],
            "recommendations": self.recommendations(),
            "created_at": datetime.now().isoformat()
        }


if __name__ == "__main__":

    agent = SEOAgent()

    result = agent.analyze(
        title="AI-COMPANY",
        description="AI Automation Platform",
        keywords=[
            "AI",
            "Automation",
            "Dashboard"
        ]
    )

    print(result)
