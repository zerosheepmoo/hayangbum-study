import {HeaderInfo, IheaderInfoParam} from './header'
interface IScreenConfig {
  width?: number
  height?: number
}
export class Screen {
  private _width: string
  private _height: string
  private _wid: number
  private _hei: number
  private _headerInfo?: HeaderInfo
  private _mainImage?: string;

  constructor(config:IScreenConfig){
    this._width = config.width ? config.width + 'px': '100%';
    this._height = config.height ? config.height + 'px': '100%';
    this._wid = config.width || 0;
    this._hei = config.height || 0;
  }

  addHeaderInfo(info: IheaderInfoParam){
    const headerInfo = new HeaderInfo(info)
    this._headerInfo = headerInfo;
  }
  addImage(imgsrcPath: string){
    this._mainImage = imgsrcPath; 
  }
  
  render(){
    // sreen 생성
    const screenEle = document.createElement('div');
    screenEle.style.width = this._width;
    screenEle.style.height = this._height;
    screenEle.className = 'cfs-screen';

    // header 생성
    if(this._headerInfo){
      const title = this._headerInfo.title ? this._headerInfo.title: 'No_Named';
      const titleEle = document.createElement('h1');
      titleEle.className = 'cfs-header'
      titleEle.textContent = title;
      titleEle.style.width = '300px'
      const twidth = 300;
      titleEle.style.left = `calc(50% - ${twidth/2}px)`;
      screenEle.appendChild(titleEle);
    }

    // 메인이미지 생성
    if(this._mainImage){
      const mainImage = new Image(this._wid, this._hei- 150);
      mainImage.src = this._mainImage;
      screenEle.appendChild(mainImage);
    }

    const alertCredit = (event:MouseEvent) => {
      alert('This is made by ZeroMoo!');
    }
    const movePage = (event: MouseEvent) => {
      location.href = "./cybershop.html";
    }

    //buttons container생성
    const buttonsContainer = document.createElement('div');
    buttonsContainer.className = 'button-container'
    screenEle.appendChild(buttonsContainer);

    // author button 생성
    const creditEle = document.createElement('button');
    creditEle.onclick = alertCredit;
    creditEle.textContent = 'About'
    buttonsContainer.appendChild(creditEle);
    
    // start button 생성
    const startEle = document.createElement('button');
    startEle.onclick = movePage;
    startEle.textContent = 'Start';
    buttonsContainer.appendChild(startEle);
    // 추가
    document.body.appendChild(screenEle);
  }
}