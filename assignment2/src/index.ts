import { Screen } from './screen'
import './style/style.css'

document.addEventListener('DOMContentLoaded', function () {
  const scre = new Screen({ width: 600, height: 400 });
  scre.addHeaderInfo({title: 'Cyber Fucking Shop'});
  scre.addImage('./main.png');
  scre.render();
})

console.log('hello, this is cfs-main page.');