# BootCamp25

## Document

- Git・GitHubの基本的なコマンドを[Document.md](./Document.md)にまとめています．
- BootCampフォルダにも[01_Git・Githubマニュアル](https://docs.google.com/document/d/1dWzkxquuMnYqfsY-4vt8KyWzTrzS2RdF897_K6X09XU/preview)として今後まとめておきます．
- [昨年時のマニュアルフォルダ](https://drive.google.com/drive/folders/1Ih7rE5o1qHnev4rD1tx0uTHA8oGwT5cO)もあります．こちらに詳細に記述したスライド等あります．
  - こちらは[Udemyの講座](https://www.udemy.com/course/unscared_git/)の受講内容をもとに作成・添付ファイルを共有しています．非常にわかりやすいのでぜひ受講をすすめます．(有料)
- 無料だと[サル先生のGit入門](https://backlog.com/ja/git-tutorial/intro/01/)が有名です．

## 前提

仮想環境を先に作っておきます．今後は以下のbootcamp内で行うことを想定しています．

```#bin/bash
mkdir bootcamp
cd bootcamp
pyenv virtualenv 3.8.10 bootcamp
pyenv local bootcamp
```

(推奨)GitHub用のssh鍵を作成します．git cloneする際はsshを指定してcloneするとパスワード要求が必要なくなり便利です．
ssh鍵の作成方法は[こちら](https://drive.google.com/file/d/1tdGc6sSylafQVrLCguFQtsufQ5UFheYv/view?usp=sharing)から確認する．

## 初期設定

ユーザー名・メールアドレス・エディタを設定します．エディタは任意ですがここではvscodeを指定ます，

```#bin/bash
git config --global user.name "hoge"
git config --global user.email "fuga"
git config --global core.editor 'code --wait'
```

にてアカウントの設定を行います。`hoge`や`fuga`のところには自分のgithubアカウントのusernameと登録したメールアドレスを入れましょう。この設定を行わないと権利関係のところで不具合が発生するので必ず行ってください。

## 使い方

こちらのリポジトリを`clone`します．

```#bin/bash
# httpsの場合(非推奨)
git clone https://github.com/keio-smilab23/BootCamp23.git
# sshの場合(推奨)
git clone git@github.com:keio-smilab23/BootCamp23.git
```

現在のブランチはmasterブランチであるので，ここからブランチを自分の作業用のブランチに切り替えます．
ブランチはここでは省略しますが，[スライドの49ページ以降](https://docs.google.com/presentation/d/1Vr8a0Rn2Vyo-sNixjIsm6ttZEAbC6oDOvk6DUUTr4Bk/edit#slide=id.p47)にまとめてあります．簡単にいうと本番用と開発用で編集するコードを切り替える感じです．

```#bin/bash
# 現在masterブランチにいることを確認
git branch
# ブランチを作成する
git branch [自分の名前]
# ブランチを[自分の名前]に切り替える
git checkout [自分の名前]
# 現在自分がいるブランチの場所を確認
git branch
```

補足ですが，ブランチを作成してそのブランチに切り替えたいときは以下のコマンドで一発でできます．

```#bin/bash
# ブランチを作成してそのブランチに切り替る
git checkout -b [新たに作成するブランチ名]
```

## 演習

実際にgitの基本的なコマンドである．`add/commit/status/push`あたりを実習してもらいます．

1. まずはBootCamp23内(現在のブランチ名が`自分の名前`であることを確認)にて[AtCoder](https://atcoder.jp/contests/abs/tasks)の問題を一問説いてください．
   - 上の方が問題としてはやさしい
   - 完璧に解けなくても大丈夫です．
   - FYI：BootCamp23のドキュメントに[スキップ可】コード品質チェッカー / Linter](https://docs.google.com/document/d/1UstCjpYozwjkRMhGJGOl6oSkXDqgAnyNlDLl3vmvmfA/edit#heading=h.5mfxlvoai28k)があるのでこちらでコード品質を確認して体裁を整えましょう．
2. ここでは`atcoder/practice.py`として作成するとします．
3. 以下のコマンドを順に実行して状態を確認していきます．**常に`git status`コマンドを打つ癖をつけましょう！**

```#bin/bash
# まず状態を確認
$ git status
On branch hatanaka
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	atcoder/

nothing added to commit but untracked files present (use "git add" to track)

# atcoder/practice.pyをインデックスに追加する
$ git add atcoder/practice.py

# 状態を確認
$ git status
On branch hatanaka
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   atcoder/practice.py

# commitしてローカルのリポジトリに追加する．
$ git commit -m "[Add]atcoder/practice.pyを作成"
[hatanaka ef00c0b] [Add]atcoder/practice.pyを作成
 1 file changed, 14 insertions(+)
 create mode 100644 atcoder/practice.py

# 状態を確認
$ git status
On branch hatanaka
nothing to commit, working tree clean

# commitのログを確認
$ git log --oneline
ef00c0b (HEAD -> hatanaka) [Add]atcoder/practice.pyを作成　// これが先程commitしたもの
8db3185 (origin/master, origin/HEAD, master) first empty commit

# 最後にリモートリポジトリ)(GitHub)に自分の最新の状態のブランチをpushする
$ git push origin hatanaka
Counting objects: 4, done.
Delta compression using up to 20 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (4/4), 534 bytes | 534.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0)
remote: 
remote: Create a pull request for 'hatanaka' on GitHub by visiting:
remote:      https://github.com/keio-smilab23/BootCamp23/pull/new/hatanaka
remote: 
To github.com:keio-smilab23/BootCamp23.git
 * [new branch]      hatanaka -> hatanaka

```

## Tips

デフォルトの場合，現在いるブランチを把握するために毎回`git branch`コマンドで確認していたかと思いますが．`~/.bashrc`ファイルに以下を追記することで現在いるブランチをターミナルに表示してくれます．

```.bashrc
# show git branch
export PS1='\[\033[01;32m\]\u@\h\[\033[01;34m\] \w \[\033[00m\]$(__git_ps1 "[%s]") \n\[\033[01;34m\]\$\[\033[00m\] '
```

`~/.bashrc`に追記したら`source ~./bashrc`を実行し再度`cd ~/bootcamp/BootCamp23`に移動するとブランチが表示されるかと思います．

```#bin/bash
# before
(Sim2Real-PonNet21) hatanakashummpei@n09 ~/00卒論/ponnet_causal_inference
# after
# [feature/delete_pred_uniter]が表示されている．
(Sim2Real-PonNet21) hatanakashummpei@n09 ~/00卒論/ponnet_causal_inference [feature/delete_pred_uniter]
```

コマンドにエイリアスをつけるとは、コマンドに別名をつけることです。git commitなど毎回打つのが面倒くさいためエイリアスをつけることでgit ciでも同じコマンドであると認識してくれるのでおすすめです。エイリアスのつけ方は

```#bin/bash
# commitの別名をciとする
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.br branch
git config --global alias.co checkout
```

となります．
