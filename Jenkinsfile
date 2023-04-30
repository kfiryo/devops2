node{
    stage("clone"){
        git "https://github.com/kfiryo/devops2.git"
    }
    stage("execute"){
        bat "dir"
        bat "python disk_resizer.py"
    }
}
