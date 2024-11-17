function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
      throw Error('Jobs is not an array');
    }
  
    const key = 'push_notification_code_3';
  
    jobs.forEach((job) => {
        const jobQueue = queue.create(key, job);
        jobQueue.save((err) => {
            if (!err) {
            console.log(`Notification job created: ${jobQueue.id}`);
    
            jobQueue.on('complete', () => {
                console.log(`Notification job ${jobQueue.id} completed`);
            });
    
            jobQueue.on('failed', (errorMessage) => {
                console.log(`Notification job ${jobQueue.id} failed: ${errorMessage}`);
            });
    
            jobQueue.on('progress', (progress) => {
                console.log(`Notification job ${jobQueue.id} ${progress}% complete`);
            });
            }
        });
    });
  }
  
export { createPushNotificationsJobs };
  