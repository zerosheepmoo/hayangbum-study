import {SFCTable} from './table'
import './style/style.css'

const tableCon: Array<string[]> = [
  ['Weapon Type', 'Weapon Name', 'Production Code', 'Price', 'etc'],
  ['Sword', 'Short-sword', 'ssd2019121400031', '3,400 G'],
  ['Bow', 'Cross-bow', 'ssd2019121100012', '8,700 G', 'Premium']
]
document.addEventListener('DOMContentLoaded', function () {
  const table = new SFCTable({height: 200, width:600, box: 5, line: 3}, tableCon)
  table.render();
});
console.log('hello, this is cfs-shop page.');

let c = document.createElement('h1')
c.className='ttitle';
c.textContent = 'Item List';
document.body.appendChild(c);



