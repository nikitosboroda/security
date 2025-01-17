from ...projects.models.statistics import Statistic
from ...tasks.api.utils import run_task


def exec_test(project_id, event):
    response = run_task(project_id, event)
    response["redirect"] = f"/task/{response['task_id']}/results"

    statistic = Statistic.query.filter_by(project_id=project_id).first()
    statistic.dast_scans += 1
    statistic.commit()

    return response
