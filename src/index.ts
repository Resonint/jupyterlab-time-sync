import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import {
  ICommandPalette
} from '@jupyterlab/apputils';

import { requestAPI } from './handler';

import moment from 'moment-timezone';

async function resync() {
  let time_data = {
    timestamp: moment().toISOString(),
    timezone: moment.tz.guess()
  }
  console.log('Syncing Time:', time_data);

  requestAPI<any>({
      method: 'POST',
      body: JSON.stringify(time_data)})
    .then(data => {
      console.log(data);
    })
    .catch(reason => {
      console.error(
        `jupyterlab_time_sync error: ${reason}`
      );
    });
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
