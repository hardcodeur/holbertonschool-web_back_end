import kue from 'kue';

const queue = kue.createQueue();
const job = {
  phoneNumber: '3167308713',
  message: 'This is the code to verify your account',
};

const queueName = 'push_notification_code';

const cli = queue.create(queueName, job).save((err) => {
    if (!err){
        console.log(`Notification job created: ${job.id}`);
    } 
});

cli.on('complete', () => {
  console.log('Notification job completed');
});

cli.on('failed', () => {
  console.log('Notification job failed');
});