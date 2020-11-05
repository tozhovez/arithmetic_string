import sys
import subprocess
from PyInquirer import prompt, Separator
from run_service import CORE_SERVICES

if __name__ == "__main__":

    try:
        questions = [
            {
                "type": "checkbox",
                "name": "service",
                "message": "Choose service",
                "choices": [*CORE_SERVICES, Separator()],
            }
        ]

        answers = prompt(questions)

        if not answers:
            sys.exit(0)

        command = [
            "docker-compose",
            "-f",
            "docker-compose.dev.yml",
            "pull",
        ]
        for service in answers["service"]:
            service_name = service.get("name")
            command.append(service_name)
        subprocess.run(command)

    except Exception as ex:
        sys.exit(1)
