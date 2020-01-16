export interface IheaderInfoParam {
  title: string;
}

export class HeaderInfo {
  private _title: string
  constructor(info: IheaderInfoParam){
    this._title = info.title;
  }
  get title(){
    return this._title;
  }
}
