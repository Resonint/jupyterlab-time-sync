import {
  JupyterFrontEnd, JupyterFrontEndPlugin
} from '@jupyterlab/application';

import {
  ICommandPalette
} from '@jupyterlab/apputils';

import moment from 'moment-timezone';

async function resync() {
  let time_data = {
    timestamp: moment().toISOString(),
    timezone: moment.tz.guess()
  }
  // console.log('Syncing Time:', time_data);

  let _xsrf = document.cookie.match("\\b_xsrf=([^;]*)\\b")[1];
  // console.log('_xsrf:', _xsrf);

  const msg = await fetch(window.location.origin+"/jupyterlab_time_sync", {
    credentials: 'same-origin',
    method: 'POST',
    body: JSON.stringify(time_data),
    headers: {
      'Content-Type': 'application/json',
      'X-XSRFToken': _xsrf
    }
  });

  if (!msg.ok)
  {
    console.error("Error");
  }
  else if (msg.status >= 400) {
    console.error('HTTP Error: '+msg.status+' - '+msg.statusText);
  } else {
    console.log('Time Sync Successful');
  }
}


/**
 * Initialization data for the jupyterlab_time_sync extension.
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab_time_sync',
  autoStart: true,
  requires: [ICommandPalette],
  activate: (app: JupyterFrontEnd, palette: ICommandPalette) => {
    console.log('JupyterLab extension jupyterlab_time_sync is activated!');

    resync(); // resync automatically on load

    // Add an application command
    const command: string = 'time_sync:run';
    app.commands.addCommand(command, {
      label: 'Resync Device to PC',
      execute: resync
    });

    // Add the command to the palette.
    palette.addItem({command, category: 'Time Sync'});
  }
};

export default extension;
