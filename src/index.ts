import {
  JupyterFrontEnd, JupyterFrontEndPlugin
} from '@jupyterlab/application';


/**
 * Initialization data for the jupyterlab_time_sync extension.
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab_time_sync',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    console.log('JupyterLab extension jupyterlab_time_sync is activated!');
  }
};

export default extension;
