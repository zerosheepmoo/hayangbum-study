interface ITableConfig {
  width?: number
  height?: number
  line: number
  box: number
}

export class SFCTable {
  private _width: string
  private _height: string
  private _wid: number
  private _hei: number
  private _boxNum: number
  private _lineNum: number
  private _tableContent: Array<string[]>

  constructor(config: ITableConfig, tableContent: Array<string[]>) {
    this._width = config.width ? config.width + 'px' : 'auto';
    this._height = config.height ? config.height + 'px' : 'auto';
    this._wid = config.width || 0;
    this._hei = config.height || 0;

    this._boxNum = config.box;
    this._lineNum = config.line;

    this._tableContent = JSON.parse(JSON.stringify(tableContent));
  }

  render() {
    // table 생성
    const outerDiv = document.createElement('div')
    outerDiv.style.width = this._width;
    outerDiv.style.height = this._height;
    const table = document.createElement('table');
    table.className = 'cfs-table';
    document.body.appendChild(outerDiv);
    outerDiv.appendChild(table);

    // thead 생성
    const thead = document.createElement('thead');
    table.appendChild(thead);
    // thead 안 tr th 생성
    const theadrow = document.createElement('tr');
    theadrow.className = 'cfs-theadrow';
    thead.appendChild(theadrow);

    const hrlen = this._tableContent[0].length;
    for (let i = 0; i < this._boxNum; i++) {
      const th = document.createElement('th');
      if (i < hrlen) {
        th.textContent = this._tableContent[0][i];
      }
      theadrow.appendChild(th);
    }

    // tbody
    const tbody = document.createElement('tbody');
    table.appendChild(tbody);

    // tr td

    for (let k = 1; k < this._lineNum; k++) {
      const rowLen = this._tableContent[k].length;
      const tr = document.createElement('tr');
      for (let j = 0; j < this._boxNum; j++) {
        const td = document.createElement('td');
        if (j < rowLen) {
          td.textContent = this._tableContent[k][j];
        }
        tr.appendChild(td);
      }
      tbody.appendChild(tr);
    }
    // movepage
    const movePage = (event: MouseEvent) => {
      location.href = "./cybermain.html";
    }
    //buttons container생성
    const buttonsContainer = document.createElement('div');
    buttonsContainer.className = 'button-container'
    outerDiv.appendChild(buttonsContainer);
    // back button
    const back = document.createElement('button');
    back.onclick = movePage;
    back.textContent = 'Back';
    buttonsContainer.appendChild(back);
    
  }
}