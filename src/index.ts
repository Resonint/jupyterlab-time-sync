import {
  JupyterFrontEnd, JupyterFrontEndPlugin
} from '@jupyterlab/application';

import {
  ICommandPalette
} from '@jupyterlab/apputils';


/**
 * Initialization data for the jupyterlab_time_sync extension.
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab_time_sync',
  autoStart: true,
  requires: [ICommandPalette],
  activate: (app: JupyterFrontEnd, palette: ICommandPalette) => {
    console.log('JupyterLab extension jupyterlab_time_sync is activated!');

    // Add an application command
    const command: string = 'time_sync:run';
    app.commands.addCommand(command, {
      label: 'Resync',
      execute: () => {
        let dt = new Date();
        console.log('Syncing Time:', dt);
      }
    });

    // Add the command to the palette.
    palette.addItem({command, category: 'Time Sync'});
  }
};

export default extension;
