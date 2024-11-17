import kue from 'kue';

const blacklist= ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  const progressMax = 100;
  job.progress(0, progressMax);

  if (blacklist.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }
  job.progress(50, progressMax);
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`,
  );
  done();
}

const queue = kue.createQueue();
const key = 'push_notification_code_2';

queue.process(key, 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});