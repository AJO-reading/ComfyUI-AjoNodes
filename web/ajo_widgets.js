
import { app } from '../../scripts/app.js'
app.registerExtension({
  name: 'ajo.widgets',

  async beforeRegisterNodeDef(nodeType, nodeData, app) {
    if (!nodeData.name.startsWith('AJO')) {
      return
    }
    switch (nodeData.name) {
      case '💾 Save Audio':
      case '🔈 Preview Audio': {
        nodeData.input.required.audioUI = ['AUDIO_UI', {}]
        break
      }
    }
  },
})
