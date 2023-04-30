properties([parameters([string(defaultValue: 'sda', name: 'DISK_NAME'), string('MACHINE_NAME'), string(defaultValue: '100', name: 'TARGET_GB')])])
node{
    stage("clone"){
        git "https://github.com/kfiryo/devops2.git"
    }
    stage("execute"){
        bat "dir"
        bat "python disk_resizer.py"
    }
}
