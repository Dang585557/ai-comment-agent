from datetime import datetime
import os


class TesterAgent:

    def test_file(self, filename: str):

        exists = os.path.exists(filename)

        return {
            "filename": filename,
            "exists": exists,
            "status": "PASSED" if exists else "FAILED",
            "tested_at": datetime.now().isoformat()
        }

    def test_directory(self, directory: str):

        exists = os.path.isdir(directory)

        files = []

        if exists:
            files = os.listdir(directory)

        return {
            "directory": directory,
            "exists": exists,
            "total_files": len(files),
            "status": "PASSED" if exists else "FAILED"
        }

    def run(self, project_paths: list):

        results = []

        for path in project_paths:

            results.append(
                self.test_file(path)
            )

        passed = sum(
            1 for result in results
            if result["status"] == "PASSED"
        )

        return {
            "total": len(results),
            "passed": passed,
            "failed": len(results) - passed,
            "results": results,
            "completed_at": datetime.now().isoformat()
        }


if __name__ == "__main__":

    tester = TesterAgent()

    print(
        tester.run(
            [
                "README.md",
                "requirements.txt"
            ]
        )
    )
