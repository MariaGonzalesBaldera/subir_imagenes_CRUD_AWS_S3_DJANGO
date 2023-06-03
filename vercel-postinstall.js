const cpx = require('child_process-promise');

async function installRequirements() {
  try {
    await cpx.exec('npm run install');
    console.log('Requirements installed successfully.');
  } catch (error) {
    console.error('Error installing requirements:', error);
  }
}

installRequirements();
