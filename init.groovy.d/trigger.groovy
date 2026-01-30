import jenkins.model.Jenkins

def jobName = 'Garage-Inspector-Auto-Pipeline'
def maxAttempts = 60
def sleepMs = 2000

def jenkins = Jenkins.getInstanceOrNull()
if (jenkins == null) {
    println "--- JENKINS NOT READY ---"
    return
}

def job = null
maxAttempts.times { i ->
    job = jenkins.getItem(jobName)
    if (job != null) return
    Thread.sleep(sleepMs)
}

if (job != null) {
    def isRunning = job.getBuilds().any { it.isBuilding() }

    def inQueue = jenkins.getQueue().getItems().any { it.task?.fullName == job.fullName }

    if (!isRunning && !inQueue) {
        println "--- STARTING AUTO-PIPELINE (${job.fullName}) ---"
        // scheduleBuild2(quietPeriod)
        job.scheduleBuild2(0)
    } else {
        println "--- PIPELINE ALREADY RUNNING OR IN QUEUE ---"
    }
} else {
    println "--- JOB '${jobName}' NOT FOUND ---"
}
