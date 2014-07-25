




<!DOCTYPE html>
<html class="   ">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    
    <title>umich_fineng/python/readFile.py at sanketh · zefyrr/umich_fineng</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <meta property="fb:app_id" content="1401488693436528"/>

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="zefyrr/umich_fineng" name="twitter:title" /><meta content="Contribute to umich_fineng development by creating an account on GitHub." name="twitter:description" /><meta content="https://avatars1.githubusercontent.com/u/5747431?s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars1.githubusercontent.com/u/5747431?s=400" property="og:image" /><meta content="zefyrr/umich_fineng" property="og:title" /><meta content="https://github.com/zefyrr/umich_fineng" property="og:url" /><meta content="Contribute to umich_fineng development by creating an account on GitHub." property="og:description" />

    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    <link rel="xhr-socket" href="/_sockets" />

    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="443CB1C4:18CF:6ECC655:53C74800" name="octolytics-dimension-request_id" /><meta content="8064427" name="octolytics-actor-id" /><meta content="sankethb" name="octolytics-actor-login" /><meta content="e3b5c9c8e9d4c4e2527a962e767359faccb32bf931cf21d55aa04ae2d84adaca" name="octolytics-actor-hash" />
    

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico" />


    <meta content="authenticity_token" name="csrf-param" />
<meta content="Uf+kBjQm81MFdL70jWykxit6igb5M/FRtosKbyD81C8m/5WrjVdN0za4EB+kCXx0PR1DlPf0pzxdJw2wFND27A==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-c534ad575b5bb8c3cc3dce9c571df7aa7400dbe9.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://assets-cdn.github.com/assets/github2-84a1b6179d461213455892ab983182bc2052a7b5.css" media="all" rel="stylesheet" type="text/css" />
    


    <meta http-equiv="x-pjax-version" content="ef2e8ad48b4c98b3a1a0065370258ac2">

      
  <meta name="description" content="Contribute to umich_fineng development by creating an account on GitHub." />


  <meta content="5747431" name="octolytics-dimension-user_id" /><meta content="zefyrr" name="octolytics-dimension-user_login" /><meta content="21479938" name="octolytics-dimension-repository_id" /><meta content="zefyrr/umich_fineng" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="21479938" name="octolytics-dimension-repository_network_root_id" /><meta content="zefyrr/umich_fineng" name="octolytics-dimension-repository_network_root_nwo" />

  <link href="https://github.com/zefyrr/umich_fineng/commits/sanketh.atom" rel="alternate" title="Recent Commits to umich_fineng:sanketh" type="application/atom+xml" />

  </head>


  <body class="logged_in  env-production windows vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" aria-label="Homepage">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


    
    <a href="/notifications" aria-label="You have no unread notifications" class="notification-indicator tooltipped tooltipped-s" data-hotkey="g n">
        <span class="mail-status all-read"></span>
</a>

      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<div class="commandbar">
  <span class="message"></span>
  <input type="text" data-hotkey="s, /" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    data-username="sankethb"
    data-repo="zefyrr/umich_fineng"
  >
  <div class="display hidden"></div>
</div>

    <input type="hidden" name="nwo" value="zefyrr/umich_fineng" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target" role="button" aria-haspopup="true">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container" aria-hidden="true">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="help tooltipped tooltipped-s" aria-label="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
        <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="https://help.github.com">Help</a></li>
        </ul>
      </div>

    

<ul id="user-links">
  <li>
    <a href="/sankethb" class="name">
      <img alt="sankethb" class=" js-avatar" data-user="8064427" height="20" src="https://avatars1.githubusercontent.com/u/8064427?s=140" width="20" /> sankethb
    </a>
  </li>

  <li class="new-menu dropdown-toggle js-menu-container">
    <a href="#" class="js-menu-target tooltipped tooltipped-s" aria-label="Create new...">
      <span class="octicon octicon-plus"></span>
      <span class="dropdown-arrow"></span>
    </a>

    <div class="new-menu-content js-menu-content">
    </div>
  </li>

  <li>
    <a href="/settings/profile" id="account_settings"
      class="tooltipped tooltipped-s"
      aria-label="Account settings (You have no verified emails)">
      <span class="octicon octicon-tools"></span>
    </a>
      <span class="octicon octicon-alert settings-warning"></span>
  </li>
  <li>
    <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="HK3AnbWPVoi7iZTEwLlnU4PfXB/cGwXKbU28pT747s+kHDl8xamOsfpscDjeecuJSXn6oFSsxwdgKZFwS4mxCg==" /></div>
      <button class="sign-out-button tooltipped tooltipped-s" aria-label="Sign out">
        <span class="octicon octicon-sign-out"></span>
      </button>
</form>  </li>

</ul>

<div class="js-new-dropdown-contents hidden">
  

<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-organization"></span> New organization</a>
  </li>


    <li class="section-title">
      <span title="zefyrr/umich_fineng">This repository</span>
    </li>
      <li>
        <a href="/zefyrr/umich_fineng/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
      </li>
</ul>

</div>


    
  </div>
</div>

      

        

<div class="flash-global js-notice flash-warn">
<div class="container">
    <h2>
      You don't have any verified emails.  We recommend <a href="https://github.com/settings/emails">verifying</a> at least one email.
    </h2>
    <p>
      Email verification helps our support team help you in case you have any email issues or lose your password.
    </p>


















</div>
</div>


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="/io/x6YdEtR0bAUZvQg8OwwIcLJBTkvg01/nzwm3sJA+MpAzcT8uUQxK8uWxBR+uftQVuxWTEIq5+1w6SjJe5g==" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="21479938" />

    <div class="select-menu js-menu-container js-select-menu">
      <a class="social-count js-social-count" href="/zefyrr/umich_fineng/watchers">
        3
      </a>
      <a href="/zefyrr/umich_fineng/subscription"
        class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0" aria-haspopup="true">
        <span class="js-select-button">
          <span class="octicon octicon-eye"></span>
          Unwatch
        </span>
      </a>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
            <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container" role="menu">

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">Be notified when participating or @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">Be notified of all conversations.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">Never be notified.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

  <li>
    

  <div class="js-toggler-container js-social-container starring-container on">

    <form accept-charset="UTF-8" action="/zefyrr/umich_fineng/unstar" class="js-toggler-form starred" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="PX+reYmfbJT0WXmjKyDeZTCYLp+modBoBXXq75u1CFK3pzwavWMtDkKNoEA6rXs4bs6qs534XF/EFsf4TIlTDw==" /></div>
      <button
        class="minibutton with-count js-toggler-target star-button"
        aria-label="Unstar this repository" title="Unstar zefyrr/umich_fineng">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/zefyrr/umich_fineng/stargazers">
          1
        </a>
</form>
    <form accept-charset="UTF-8" action="/zefyrr/umich_fineng/star" class="js-toggler-form unstarred" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="+lKQ7tTD0m7Hy+HX/Ul02cLKQZCOug9ErIktuPuhTd1sdOG0cXw/Hode2L4e8yAutSqYsgFYUjkXOc508zhqKw==" /></div>
      <button
        class="minibutton with-count js-toggler-target star-button"
        aria-label="Star this repository" title="Star zefyrr/umich_fineng">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/zefyrr/umich_fineng/stargazers">
          1
        </a>
</form>  </div>

  </li>


        <li>
          <a href="/zefyrr/umich_fineng/fork" class="minibutton with-count js-toggler-target fork-button lighter tooltipped-n" title="Fork your own copy of zefyrr/umich_fineng to your account" aria-label="Fork your own copy of zefyrr/umich_fineng to your account" rel="nofollow" data-method="post">
            <span class="octicon octicon-repo-forked"></span>
            Fork
          </a>
          <a href="/zefyrr/umich_fineng/network" class="social-count">1</a>
        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/zefyrr" class="url fn" itemprop="url" rel="author"><span itemprop="title">zefyrr</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/zefyrr/umich_fineng" class="js-current-repository js-repo-home-link">umich_fineng</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline js-new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Code">
        <a href="/zefyrr/umich_fineng/tree/sanketh" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /zefyrr/umich_fineng/tree/sanketh">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped tooltipped-w" aria-label="Issues">
          <a href="/zefyrr/umich_fineng/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g i" data-selected-links="repo_issues /zefyrr/umich_fineng/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>0</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
        <a href="/zefyrr/umich_fineng/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g p" data-selected-links="repo_pulls /zefyrr/umich_fineng/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


        <li class="tooltipped tooltipped-w" aria-label="Wiki">
          <a href="/zefyrr/umich_fineng/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g w" data-selected-links="repo_wiki /zefyrr/umich_fineng/wiki">
            <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped tooltipped-w" aria-label="Pulse">
        <a href="/zefyrr/umich_fineng/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /zefyrr/umich_fineng/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Graphs">
        <a href="/zefyrr/umich_fineng/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /zefyrr/umich_fineng/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Network">
        <a href="/zefyrr/umich_fineng/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /zefyrr/umich_fineng/network">
          <span class="octicon octicon-repo-forked"></span> <span class="full-word">Network</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=push">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/zefyrr/umich_fineng.git" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/zefyrr/umich_fineng.git" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=push">
  <h3><strong>SSH</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="git@github.com:zefyrr/umich_fineng.git" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="git@github.com:zefyrr/umich_fineng.git" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=push">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/zefyrr/umich_fineng" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/zefyrr/umich_fineng" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>


  <a href="github-windows://openRepo/https://github.com/zefyrr/umich_fineng" class="minibutton sidebar-button" title="Save zefyrr/umich_fineng to your computer and use it in GitHub Desktop." aria-label="Save zefyrr/umich_fineng to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>

                <a href="/zefyrr/umich_fineng/archive/sanketh.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download zefyrr/umich_fineng as a zip file"
                   title="Download zefyrr/umich_fineng as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<a href="/zefyrr/umich_fineng/blob/b7e4deac840941792be5656ac2fe96764b7b21e2/python/readFile.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:f06f958eef2c0b0718c746f7cb5e414a -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="sanketh"
    title="sanketh"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">sanketh</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/zefyrr/umich_fineng/blob/master/python/readFile.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/zefyrr/umich_fineng/blob/omerk/python/readFile.py"
                 data-name="omerk"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="omerk">omerk</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/zefyrr/umich_fineng/blob/sanketh/python/readFile.py"
                 data-name="sanketh"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="sanketh">sanketh</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/zefyrr/umich_fineng/blob/sindhu/python/readFile.py"
                 data-name="sindhu"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="sindhu">sindhu</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <form accept-charset="UTF-8" action="/zefyrr/umich_fineng/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="x9EJFnyecn0pwVtt2mFyBfR3X5IM0//DyNNL/kyrETGT8AJDse6ULocK+TeRx/RkAPMRLZTqmKN2G8rZmjPbvw==" /></div>
            <span class="octicon octicon-git-branch select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <h4>Create branch: <span class="js-new-item-name"></span></h4>
              <span class="description">from ‘sanketh’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="sanketh" />
            <input type="hidden" name="path" id="path" value="python/readFile.py" />
          </form> <!-- /.select-menu-item -->

      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="button-group right">
    <a href="/zefyrr/umich_fineng/find/sanketh"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button class="js-zeroclipboard minibutton zeroclipboard-button"
          data-clipboard-text="python/readFile.py"
          aria-label="Copy to clipboard"
          data-copied-hint="Copied!">
      <span class="octicon octicon-clippy"></span>
    </button>
  </div>

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/zefyrr/umich_fineng/tree/sanketh" data-branch="sanketh" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">umich_fineng</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/zefyrr/umich_fineng/tree/sanketh/python" data-branch="sanketh" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">python</span></a></span><span class="separator"> / </span><strong class="final-path">readFile.py</strong>
  </div>
</div>


  <div class="commit file-history-tease">
      <img alt="sankethb" class="main-avatar js-avatar" data-user="8064427" height="24" src="https://avatars1.githubusercontent.com/u/8064427?s=140" width="24" />
      <span class="author"><a href="/sankethb" rel="contributor">sankethb</a></span>
      <time datetime="2014-07-14T19:18:58-04:00" is="relative-time">July 14, 2014</time>
      <div class="commit-title">
          <a href="/zefyrr/umich_fineng/commit/b7e4deac840941792be5656ac2fe96764b7b21e2" class="message" data-pjax="true" title="Includes delta and gamma calculations

central difference delta and non uniform grid gamma">Includes delta and gamma calculations</a>
      </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong>  contributor</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="sankethb" class=" js-avatar" data-user="8064427" height="24" src="https://avatars1.githubusercontent.com/u/8064427?s=140" width="24" />
            <a href="/sankethb">sankethb</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
        <span class="meta-divider"></span>
          <span>190 lines (134 sloc)</span>
          <span class="meta-divider"></span>
        <span>6.707 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
            <a class="minibutton tooltipped tooltipped-w"
               href="github-windows://openRepo/https://github.com/zefyrr/umich_fineng?branch=sanketh&amp;filepath=python%2FreadFile.py" aria-label="Open this file in GitHub for Windows">
                <span class="octicon octicon-device-desktop"></span> Open
            </a>
                <a class="minibutton js-update-url-with-hash"
                   href="/zefyrr/umich_fineng/edit/sanketh/python/readFile.py"
                   data-method="post" rel="nofollow" data-hotkey="e">Edit</a>
          <a href="/zefyrr/umich_fineng/raw/sanketh/python/readFile.py" class="minibutton " id="raw-url">Raw</a>
            <a href="/zefyrr/umich_fineng/blame/sanketh/python/readFile.py" class="minibutton js-update-url-with-hash">Blame</a>
          <a href="/zefyrr/umich_fineng/commits/sanketh/python/readFile.py" class="minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->

            <a class="minibutton danger empty-icon"
               href="/zefyrr/umich_fineng/delete/sanketh/python/readFile.py"
               data-method="post" data-test-id="delete-blob-file" rel="nofollow">

          Delete
        </a>
      </div><!-- /.actions -->
    </div>
      
  <div class="blob-wrapper data type-python js-blob-data">
       <table class="file-code file-diff tab-size-8">
         <tr class="file-code-line">
           <td class="blob-line-nums">
             <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>

           </td>
           <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line' id='LC1'><span class="kn">import</span> <span class="nn">os</span><span class="o">,</span> <span class="nn">re</span><span class="o">,</span> <span class="nn">subprocess</span></div><div class='line' id='LC2'><span class="kn">import</span> <span class="nn">fileinput</span><span class="o">,</span> <span class="nn">time</span></div><div class='line' id='LC3'><span class="kn">import</span> <span class="nn">argparse</span></div><div class='line' id='LC4'><span class="kn">import</span> <span class="nn">fnmatch</span></div><div class='line' id='LC5'><span class="kn">import</span> <span class="nn">tick_pb2</span> <span class="kn">as</span> <span class="nn">proto</span></div><div class='line' id='LC6'><span class="kn">import</span> <span class="nn">varint</span></div><div class='line' id='LC7'><span class="kn">import</span> <span class="nn">csv</span></div><div class='line' id='LC8'><br/></div><div class='line' id='LC9'><br/></div><div class='line' id='LC10'><span class="k">def</span> <span class="nf">getInstrumentIterator</span><span class="p">(</span><span class="nb">input</span><span class="p">):</span></div><div class='line' id='LC11'>	<span class="n">inputFh</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="nb">input</span><span class="p">,</span> <span class="s">&quot;rb&quot;</span><span class="p">)</span></div><div class='line' id='LC12'>	<span class="n">data</span>  <span class="o">=</span> <span class="n">inputFh</span><span class="o">.</span><span class="n">read</span><span class="p">()</span></div><div class='line' id='LC13'>	<span class="n">decoder</span> <span class="o">=</span> <span class="n">varint</span><span class="o">.</span><span class="n">decodeVarint32</span></div><div class='line' id='LC14'>	<span class="n">next_pos</span><span class="p">,</span> <span class="n">pos</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span></div><div class='line' id='LC15'>	<span class="c"># Loop to read each pricedData object in the file</span></div><div class='line' id='LC16'><br/></div><div class='line' id='LC17'>	<span class="n">pricedData</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC18'>	<span class="n">lastOptionMeta</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC19'>	<span class="k">while</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC20'>		<span class="n">pricedRecord</span> <span class="o">=</span> <span class="n">proto</span><span class="o">.</span><span class="n">PricedRecord</span><span class="p">()</span></div><div class='line' id='LC21'><br/></div><div class='line' id='LC22'>		<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC23'>			<span class="n">next_pos</span><span class="p">,</span> <span class="n">pos</span> <span class="o">=</span> <span class="n">decoder</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">pos</span><span class="p">)</span></div><div class='line' id='LC24'>		<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC25'>			<span class="k">break</span></div><div class='line' id='LC26'>		<span class="n">pricedRecord</span><span class="o">.</span><span class="n">ParseFromString</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="n">pos</span><span class="p">:</span><span class="n">pos</span> <span class="o">+</span> <span class="n">next_pos</span><span class="p">])</span></div><div class='line' id='LC27'>		<span class="n">pos</span> <span class="o">+=</span> <span class="n">next_pos</span></div><div class='line' id='LC28'><br/></div><div class='line' id='LC29'>		<span class="n">optionMeta</span> <span class="o">=</span> <span class="n">pricedRecord</span><span class="o">.</span><span class="n">pairedTick</span><span class="o">.</span><span class="n">optionMeta</span></div><div class='line' id='LC30'>		<span class="k">if</span> <span class="n">lastOptionMeta</span><span class="p">:</span></div><div class='line' id='LC31'>			<span class="k">if</span> <span class="n">lastOptionMeta</span><span class="o">.</span><span class="n">instrument</span> <span class="o">!=</span>  <span class="n">optionMeta</span><span class="o">.</span><span class="n">instrument</span><span class="p">:</span></div><div class='line' id='LC32'>				<span class="k">yield</span> <span class="p">(</span><span class="n">lastOptionMeta</span><span class="p">,</span> <span class="n">pricedData</span><span class="p">)</span></div><div class='line' id='LC33'>				<span class="n">pricedData</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC34'><br/></div><div class='line' id='LC35'>		<span class="n">pricedData</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">pricedRecord</span><span class="p">)</span></div><div class='line' id='LC36'>		<span class="n">lastOptionMeta</span> <span class="o">=</span> <span class="n">optionMeta</span></div><div class='line' id='LC37'><br/></div><div class='line' id='LC38'>	<span class="n">inputFh</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC39'>	<span class="k">yield</span> <span class="p">(</span><span class="n">lastOptionMeta</span><span class="p">,</span> <span class="n">pricedData</span><span class="p">)</span></div><div class='line' id='LC40'><br/></div><div class='line' id='LC41'><br/></div><div class='line' id='LC42'><span class="k">def</span> <span class="nf">getTimeInSecs</span><span class="p">(</span><span class="n">timeStr</span><span class="p">):</span></div><div class='line' id='LC43'>	<span class="n">time</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="nb">int</span><span class="p">(</span><span class="n">x</span><span class="p">),</span>  <span class="n">timeStr</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;:&#39;</span><span class="p">))</span></div><div class='line' id='LC44'>	<span class="n">timeSecs</span> <span class="o">=</span> <span class="p">(</span><span class="n">time</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="mi">24</span> <span class="o">*</span> <span class="mi">60</span><span class="p">)</span> <span class="o">+</span> <span class="p">(</span><span class="n">time</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">*</span> <span class="mi">60</span><span class="p">)</span> <span class="o">+</span> <span class="n">time</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span></div><div class='line' id='LC45'>	<span class="k">return</span> <span class="n">timeSecs</span></div><div class='line' id='LC46'><br/></div><div class='line' id='LC47'><br/></div><div class='line' id='LC48'><span class="k">def</span> <span class="nf">createPositions</span><span class="p">(</span><span class="n">pricedData</span><span class="p">):</span></div><div class='line' id='LC49'>	<span class="n">positionsIndex</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC50'><br/></div><div class='line' id='LC51'>	<span class="n">startPositionIndex</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC52'>	<span class="n">endPositionIndex</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC53'><br/></div><div class='line' id='LC54'>	<span class="n">i</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC55'>	<span class="k">for</span> <span class="n">pricedRecord</span> <span class="ow">in</span> <span class="n">pricedData</span><span class="p">:</span></div><div class='line' id='LC56'>		<span class="n">timeSecs</span> <span class="o">=</span> <span class="n">getTimeInSecs</span><span class="p">(</span><span class="n">pricedRecord</span><span class="o">.</span><span class="n">pairedTick</span><span class="o">.</span><span class="n">optionTick</span><span class="o">.</span><span class="n">timestampStr</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">)[</span><span class="mi">1</span><span class="p">])</span></div><div class='line' id='LC57'><br/></div><div class='line' id='LC58'>		<span class="k">if</span> <span class="ow">not</span> <span class="n">startPositionIndex</span><span class="p">:</span></div><div class='line' id='LC59'>			<span class="k">if</span> <span class="n">timeSecs</span> <span class="o">&gt;</span> <span class="n">getTimeInSecs</span><span class="p">(</span><span class="s">&#39;09:45:00&#39;</span><span class="p">):</span></div><div class='line' id='LC60'>				<span class="n">startPositionIndex</span> <span class="o">=</span> <span class="n">i</span></div><div class='line' id='LC61'><br/></div><div class='line' id='LC62'>		<span class="k">if</span> <span class="ow">not</span> <span class="n">endPositionIndex</span><span class="p">:</span></div><div class='line' id='LC63'>			<span class="k">if</span> <span class="n">timeSecs</span> <span class="o">&gt;</span> <span class="n">getTimeInSecs</span><span class="p">(</span><span class="s">&#39;15:30:00&#39;</span><span class="p">):</span></div><div class='line' id='LC64'>				<span class="n">endPositionIndex</span> <span class="o">=</span> <span class="n">i</span></div><div class='line' id='LC65'>				<span class="k">break</span></div><div class='line' id='LC66'><br/></div><div class='line' id='LC67'>		<span class="n">i</span> <span class="o">=</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span></div><div class='line' id='LC68'><br/></div><div class='line' id='LC69'>	<span class="k">if</span> <span class="n">startPositionIndex</span> <span class="ow">and</span> <span class="n">endPositionIndex</span><span class="p">:</span></div><div class='line' id='LC70'>			<span class="n">positionsIndex</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">startPositionIndex</span><span class="p">,</span> <span class="n">endPositionIndex</span><span class="p">))</span></div><div class='line' id='LC71'><br/></div><div class='line' id='LC72'>	<span class="k">return</span> <span class="n">positionsIndex</span></div><div class='line' id='LC73'><br/></div><div class='line' id='LC74'><span class="k">def</span> <span class="nf">processPosition</span><span class="p">(</span><span class="n">pricedData</span><span class="p">,</span> <span class="n">positionIndex</span><span class="p">):</span></div><div class='line' id='LC75'>	<span class="p">(</span><span class="n">startPositionIndex</span><span class="p">,</span> <span class="n">endPositionIndex</span><span class="p">)</span> <span class="o">=</span> <span class="n">positionIndex</span></div><div class='line' id='LC76'>	<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">startPositionIndex</span><span class="p">,</span> <span class="n">endPositionIndex</span><span class="p">):</span></div><div class='line' id='LC77'>		<span class="n">pricedRecord_t0</span> <span class="o">=</span> <span class="n">pricedData</span><span class="p">[</span><span class="n">i</span><span class="p">]</span></div><div class='line' id='LC78'>		<span class="n">pricedRecord_t1</span> <span class="o">=</span> <span class="n">pricedData</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pricedRecord_t2</span> <span class="o">=</span> <span class="n">pricedData</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">2</span><span class="p">]</span></div><div class='line' id='LC80'><br/></div><div class='line' id='LC81'>		<span class="n">underlyingTick_t0</span> <span class="o">=</span> <span class="n">pricedRecord_t0</span><span class="o">.</span><span class="n">pairedTick</span><span class="o">.</span><span class="n">underlyingTick</span></div><div class='line' id='LC82'>		<span class="n">underlyingTick_t1</span> <span class="o">=</span> <span class="n">pricedRecord_t1</span><span class="o">.</span><span class="n">pairedTick</span><span class="o">.</span><span class="n">underlyingTick</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">underlyingTick_t2</span> <span class="o">=</span> <span class="n">pricedRecord_t2</span><span class="o">.</span><span class="n">pairedTick</span><span class="o">.</span><span class="n">underlyingTick</span></div><div class='line' id='LC84'><br/></div><div class='line' id='LC85'>		<span class="n">optionTick_t0</span> <span class="o">=</span> <span class="n">pricedRecord_t0</span><span class="o">.</span><span class="n">pairedTick</span><span class="o">.</span><span class="n">optionTick</span></div><div class='line' id='LC86'>		<span class="n">optionTick_t1</span> <span class="o">=</span> <span class="n">pricedRecord_t1</span><span class="o">.</span><span class="n">pairedTick</span><span class="o">.</span><span class="n">optionTick</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">optionTick_t2</span> <span class="o">=</span> <span class="n">pricedRecord_t2</span><span class="o">.</span><span class="n">pairedTick</span><span class="o">.</span><span class="n">optionTick</span>	           </div><div class='line' id='LC88'><br/></div><div class='line' id='LC89'><br/></div><div class='line' id='LC90'>		<span class="n">underlyingLastDiff</span> <span class="o">=</span> <span class="p">(</span><span class="n">underlyingTick_t0</span><span class="o">.</span><span class="n">ask</span> <span class="o">-</span> <span class="n">underlyingTick_t1</span><span class="o">.</span><span class="n">ask</span><span class="p">)</span> <span class="o">+</span> <span class="p">(</span><span class="n">underlyingTick_t0</span><span class="o">.</span><span class="n">bid</span> <span class="o">-</span> <span class="n">underlyingTick_t1</span><span class="o">.</span><span class="n">bid</span><span class="p">)</span></div><div class='line' id='LC91'>		<span class="n">optionLastDiff</span> <span class="o">=</span> <span class="p">(</span><span class="n">optionTick_t0</span><span class="o">.</span><span class="n">ask</span> <span class="o">-</span> <span class="n">optionTick_t1</span><span class="o">.</span><span class="n">ask</span><span class="p">)</span> <span class="o">+</span> <span class="p">(</span><span class="n">optionTick_t0</span><span class="o">.</span><span class="n">bid</span> <span class="o">-</span> <span class="n">optionTick_t1</span><span class="o">.</span><span class="n">bid</span><span class="p">)</span></div><div class='line' id='LC92'><br/></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#distOne = ((underlyingTick_t1.last - underlyingTick_t0.last) + (underlyingTick_t1.bid - underlyingTick_t0.bid))/2</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#distTwo = ((underlyingTick_t2.ask - underlyingTick_t1.ask) + (underlyingTick_t2.bid - underlyingTick_t1.bid))/2</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">distOne</span> <span class="o">=</span> <span class="p">(</span><span class="n">underlyingTick_t1</span><span class="o">.</span><span class="n">last</span> <span class="o">-</span> <span class="n">underlyingTick_t0</span><span class="o">.</span><span class="n">last</span><span class="p">)</span> </div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">distTwo</span> <span class="o">=</span> <span class="p">(</span><span class="n">underlyingTick_t2</span><span class="o">.</span><span class="n">last</span> <span class="o">-</span> <span class="n">underlyingTick_t1</span><span class="o">.</span><span class="n">last</span><span class="p">)</span></div><div class='line' id='LC98'><br/></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#underlyingcentraldiff = </span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#optioncentraldiff = </span></div><div class='line' id='LC101'><br/></div><div class='line' id='LC102'>		<span class="c"># underlyingLastDiff = underlyingTick_t0.last - underlyingTick_t1.last</span></div><div class='line' id='LC103'>		<span class="c"># optionLastDiff = optionTick_t0.last - optionTick_t1.last</span></div><div class='line' id='LC104'><br/></div><div class='line' id='LC105'>		<span class="c"># Skipping deltas that have experienced no change</span></div><div class='line' id='LC106'>		<span class="k">if</span> <span class="n">underlyingLastDiff</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">or</span> <span class="n">optionLastDiff</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC107'>			<span class="k">print</span> <span class="s">&#39;Skipping delta calculation at index (</span><span class="si">%d</span><span class="s">,</span><span class="si">%d</span><span class="s">), due to no change in quotes&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC108'>			<span class="k">continue</span></div><div class='line' id='LC109'><br/></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">distOne</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">or</span> <span class="n">distTwo</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC111'>			<span class="k">print</span> <span class="s">&#39;Skipping delta calculation at index (</span><span class="si">%d</span><span class="s">,</span><span class="si">%d</span><span class="s">), due to no change in quotes&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC112'>			<span class="k">continue</span></div><div class='line' id='LC113'><br/></div><div class='line' id='LC114'>		<span class="n">observedDelta</span> <span class="o">=</span> <span class="n">optionLastDiff</span><span class="o">/</span><span class="n">underlyingLastDiff</span></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#opt_t0 = (optionTick_t0.ask + optionTick_t0.bid)/2                </span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#opt_t1 = (optionTick_t1.ask + optionTick_t1.bid)/2</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#opt_t2 = (optionTick_t2.ask + optionTick_t2.bid)/2</span></div><div class='line' id='LC119'><br/></div><div class='line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">opt_t0</span> <span class="o">=</span> <span class="n">optionTick_t0</span><span class="o">.</span><span class="n">last</span>                </div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">opt_t1</span> <span class="o">=</span> <span class="n">optionTick_t1</span><span class="o">.</span><span class="n">last</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">opt_t2</span> <span class="o">=</span> <span class="n">optionTick_t2</span><span class="o">.</span><span class="n">last</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">observedCentralDelta</span> <span class="o">=</span> <span class="p">(</span><span class="n">opt_t2</span> <span class="o">-</span> <span class="p">((</span><span class="n">distTwo</span><span class="o">/</span><span class="n">distOne</span><span class="p">)</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span><span class="o">*</span><span class="n">opt_t0</span> <span class="o">-</span> <span class="p">(</span><span class="mi">1</span> <span class="o">-</span> <span class="p">(</span><span class="n">distTwo</span><span class="o">/</span><span class="n">distOne</span><span class="p">)</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span><span class="o">*</span><span class="n">opt_t1</span><span class="p">)</span><span class="o">/</span><span class="p">(</span><span class="n">distTwo</span><span class="o">*</span><span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="p">(</span><span class="n">distTwo</span><span class="o">/</span><span class="n">distOne</span><span class="p">)))</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#observedCentralDelta2 = ((-distTwo)/((distOne)*(distOne + distTwo)))*opt                            </span></div><div class='line' id='LC126'><br/></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">observedGamma</span> <span class="o">=</span> <span class="mi">2</span><span class="o">*</span><span class="p">(</span><span class="n">opt_t2</span> <span class="o">+</span> <span class="p">(</span><span class="n">distTwo</span><span class="o">/</span><span class="n">distOne</span><span class="p">)</span><span class="o">*</span><span class="n">opt_t2</span> <span class="o">-</span> <span class="p">(</span><span class="mi">1</span><span class="o">+</span><span class="p">(</span><span class="n">distTwo</span><span class="o">/</span><span class="n">distOne</span><span class="p">))</span><span class="o">*</span><span class="n">opt_t1</span><span class="p">)</span><span class="o">/</span><span class="p">(</span><span class="n">distOne</span><span class="o">*</span><span class="n">distTwo</span><span class="o">*</span><span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="p">(</span><span class="n">distTwo</span><span class="o">/</span><span class="n">distOne</span><span class="p">)))</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writer</span> <span class="o">=</span> <span class="n">csv</span><span class="o">.</span><span class="n">writer</span><span class="p">(</span><span class="nb">open</span><span class="p">(</span><span class="s">&#39;sankethlist.csv&#39;</span><span class="p">,</span><span class="s">&#39;wb&#39;</span><span class="p">))</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writer</span><span class="o">.</span><span class="n">writerow</span><span class="p">([</span><span class="s">&#39;id&#39;</span><span class="p">,</span> <span class="s">&#39;deviation&#39;</span><span class="p">,</span> <span class="s">&#39;deviation with central&#39;</span><span class="p">,</span> <span class="s">&#39;empirical&#39;</span><span class="p">,</span> <span class="s">&#39;emp with central&#39;</span><span class="p">,</span> <span class="s">&#39;theoretical&#39;</span><span class="p">,</span> <span class="s">&#39;gamma&#39;</span><span class="p">,</span> <span class="s">&#39;stockLast&#39;</span><span class="p">])</span>                  		</div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#deviationList = []</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">deviationList</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC134'>		<span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">pricedRecord_t0</span><span class="o">.</span><span class="n">theoreticals</span><span class="p">)):</span></div><div class='line' id='LC135'>			<span class="n">theoretical</span> <span class="o">=</span> <span class="n">pricedRecord_t0</span><span class="o">.</span><span class="n">theoreticals</span><span class="p">[</span><span class="n">j</span><span class="p">]</span></div><div class='line' id='LC136'><br/></div><div class='line' id='LC137'><br/></div><div class='line' id='LC138'>			<span class="n">deviation</span> <span class="o">=</span> <span class="nb">abs</span><span class="p">(</span><span class="n">observedDelta</span> <span class="o">-</span> <span class="n">theoretical</span><span class="o">.</span><span class="n">delta</span><span class="p">)</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">deviation2</span> <span class="o">=</span> <span class="nb">abs</span><span class="p">(</span><span class="n">observedCentralDelta</span> <span class="o">-</span> <span class="n">theoretical</span><span class="o">.</span><span class="n">delta</span><span class="p">)</span></div><div class='line' id='LC140'><br/></div><div class='line' id='LC141'>			<span class="n">deviationList</span><span class="o">.</span><span class="n">append</span><span class="p">({</span><span class="s">&#39;id&#39;</span><span class="p">:</span> <span class="n">theoretical</span><span class="o">.</span><span class="n">Id</span><span class="o">.</span><span class="n">numDataPoints</span><span class="p">,</span> <span class="s">&#39;deviation&#39;</span><span class="p">:</span> <span class="n">deviation</span><span class="p">,</span> <span class="s">&#39;deviation with central&#39;</span><span class="p">:</span> <span class="n">deviation2</span><span class="p">,</span> <span class="s">&#39;empirical&#39;</span><span class="p">:</span> <span class="n">observedDelta</span><span class="p">,</span> <span class="s">&#39;emp with central&#39;</span><span class="p">:</span> <span class="n">observedCentralDelta</span><span class="p">,</span> <span class="s">&#39;theoretical&#39;</span><span class="p">:</span> <span class="n">theoretical</span><span class="o">.</span><span class="n">delta</span><span class="p">,</span> <span class="s">&#39;stockLast&#39;</span><span class="p">:</span> <span class="n">underlyingTick_t0</span><span class="o">.</span><span class="n">last</span><span class="p">})</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writer</span><span class="o">.</span><span class="n">writerow</span><span class="p">([</span><span class="n">theoretical</span><span class="o">.</span><span class="n">Id</span><span class="o">.</span><span class="n">numDataPoints</span><span class="p">,</span> <span class="n">deviation</span><span class="p">,</span> <span class="n">deviation2</span><span class="p">,</span> <span class="n">observedDelta</span><span class="p">,</span> <span class="n">observedCentralDelta</span><span class="p">,</span> <span class="n">theoretical</span><span class="o">.</span><span class="n">delta</span><span class="p">,</span> <span class="n">observedGamma</span><span class="p">,</span> <span class="n">underlyingTick_t0</span><span class="o">.</span><span class="n">last</span><span class="p">])</span></div><div class='line' id='LC143'>			<span class="c">#theoreticalPrice = theoretical.price</span></div><div class='line' id='LC144'>		<span class="n">deviationList</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="s">&#39;deviation with central&#39;</span><span class="p">])</span></div><div class='line' id='LC145'><br/></div><div class='line' id='LC146'>		<span class="k">print</span> <span class="n">deviationList</span><span class="p">[:</span><span class="mi">10</span><span class="p">]</span></div><div class='line' id='LC147'><br/></div><div class='line' id='LC148'><br/></div><div class='line' id='LC149'><br/></div><div class='line' id='LC150'><br/></div><div class='line' id='LC151'><span class="k">def</span> <span class="nf">processInstrument</span><span class="p">(</span><span class="n">optionMeta</span><span class="p">,</span> <span class="n">pricedData</span><span class="p">):</span></div><div class='line' id='LC152'>	<span class="k">print</span> <span class="s">&#39;Processing -&#39;</span><span class="p">,</span> <span class="n">optionMeta</span></div><div class='line' id='LC153'><br/></div><div class='line' id='LC154'>	<span class="n">positions</span> <span class="o">=</span> <span class="n">createPositions</span><span class="p">(</span><span class="n">pricedData</span><span class="p">)</span></div><div class='line' id='LC155'>	<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">positions</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC156'>		<span class="k">print</span> <span class="s">&#39;No positions found&#39;</span></div><div class='line' id='LC157'>		<span class="k">return</span> </div><div class='line' id='LC158'><br/></div><div class='line' id='LC159'>	<span class="k">for</span> <span class="n">positionIndex</span> <span class="ow">in</span> <span class="n">positions</span><span class="p">:</span></div><div class='line' id='LC160'>		<span class="n">processPosition</span><span class="p">(</span><span class="n">pricedData</span><span class="p">,</span> <span class="n">positionIndex</span><span class="p">)</span></div><div class='line' id='LC161'><br/></div><div class='line' id='LC162'><br/></div><div class='line' id='LC163'><br/></div><div class='line' id='LC164'><span class="k">def</span> <span class="nf">main</span><span class="p">():</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#parser = argparse.ArgumentParser(description=&quot;Run analysis&quot;)</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#parser.add_argument(&#39;-d&#39;, &#39;--datadir&#39;, help=&#39;location of priced data&#39;)</span></div><div class='line' id='LC167'><br/></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#args = parser.parse_args()</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC170'><span class="c">#    if not args.datadir:</span></div><div class='line' id='LC171'><span class="c">#    	parser.print_help()</span></div><div class='line' id='LC172'><span class="c">#    	return</span></div><div class='line' id='LC173'><span class="c">#</span></div><div class='line' id='LC174'><span class="c">#    if not os.path.exists(args.datadir):</span></div><div class='line' id='LC175'><span class="c">#    	print &#39;Invalid path %s&#39; % args.datadir</span></div><div class='line' id='LC176'><span class="c">#    	return</span></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC178'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;check&#39;</span></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">root</span><span class="p">,</span> <span class="n">dirnames</span><span class="p">,</span> <span class="n">filenames</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">walk</span><span class="p">(</span><span class="s">&quot;C://Trading//data//analysis_20140628//FDX.priced//FDX//FDX//20140610&quot;</span><span class="p">):</span></div><div class='line' id='LC180'>&nbsp;&nbsp;&nbsp;&nbsp;	<span class="k">for</span> <span class="n">filename</span> <span class="ow">in</span> <span class="n">fnmatch</span><span class="o">.</span><span class="n">filter</span><span class="p">(</span><span class="n">filenames</span><span class="p">,</span> <span class="s">&#39;option_tick_priced.proto&#39;</span><span class="p">):</span></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;		<span class="n">pricedDataFile</span> <span class="o">=</span> <span class="n">root</span> <span class="o">+</span> <span class="s">&quot;//&quot;</span> <span class="o">+</span> <span class="n">filename</span></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;		<span class="k">print</span> <span class="s">&#39;Processing file -&#39;</span><span class="p">,</span> <span class="n">pricedDataFile</span> </div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;		<span class="k">for</span> <span class="p">(</span><span class="n">optionMeta</span><span class="p">,</span> <span class="n">pricedData</span><span class="p">)</span> <span class="ow">in</span> <span class="n">getInstrumentIterator</span><span class="p">(</span><span class="n">pricedDataFile</span><span class="p">):</span></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;			<span class="n">processInstrument</span><span class="p">(</span><span class="n">optionMeta</span><span class="p">,</span> <span class="n">pricedData</span><span class="p">)</span></div><div class='line' id='LC185'><br/></div><div class='line' id='LC186'>&nbsp;</div><div class='line' id='LC187'><br/></div><div class='line' id='LC188'><br/></div><div class='line' id='LC189'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">main</span><span class="p">()</span></div></pre></div></td>
         </tr>
       </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.04473s from github-fe123-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-df9e4beac80276ed3dfa56be0d97b536d0f5ee12.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-534eef699bbadaf1454b432e14a2ab0a68c7ddf4.js" type="text/javascript"></script>
      
      
        <script async src="https://www.google-analytics.com/analytics.js"></script>
  </body>
</html>

