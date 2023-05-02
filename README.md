# convert-mpeg-mp4
mpegをmp4に変換する<br>
<br>
(made with chatgpt)<br>
<br>
前提条件として以下の環境を用意する<br>
1.ffmpeg<br>
2.python<br>
<br>
次に、環境変数を設定、PATHに以下を追記<br>
C:\Python<br>
C:\ffmpeg\bin<br>
C:\work\python<br>
最後の行(C:\work\python)は後述する変換スクリプトの置き場所により変更する<br>
<br>
<br>
スクリプト配置場所
C:\work\python\convert_mpeg_mp4.py
<br>
使い方<br>
1.スクリプト設置場所フォルダ内にconfig.txtがあるので、<br>
　変換に必要なパラメータを指定する<br>
2.convert_mpeg_mp4.pyをダブルクリックで実行すると、エクスプローラーが開くので、<br>
3.mp4に変換したいmpegを選択する。（config.txtに映像・音声の仕様を記載する）<br>
 （複数選択する場合は、ctrlやshiftなどのボタンを使って複数選択する）<br>
4.選択後、再度、エクスプローラーが開くので、保存先とするフォルダを指定する。<br>
<br>
コマンドプロンプト画面が表示されて、変換状況が表示される。<br>
このとき、保存先フォルダに同一ファイル名のmp4がある場合は、<br>
上書き保存について聞かれるので、y/Nで答える。<br>
<br>
変換が終わると、コマンドプロンプトが消えるので変換は終了。<br>
<br>
補足：<br>
　ダブルクリックで実行できないなどあれば、<br>
　powershellを起動して、コマンドラインで実行してみる。<br>
　エラーの内容が表示されるのでchatgptに聞いてみる。<br>

