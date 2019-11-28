#!/usr/bin/env python3
import os
from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    os.environ['CONAN_CMAKE_GENERATOR']='Ninja'
    builder = ConanMultiPackager(
        docker_run_options='-v "$HOME/.conan/data:/home/conan/.conan/data"',
        pip_install=['ninja'],

        username="Artalus",
        channel='ci',
        remotes="https://api.bintray.com/conan/bincrafters/public-conan",
        build_policy='missing',

        upload="https://api.bintray.com/conan/artalus/conan-public",
        stable_branch_pattern="release/*",
        upload_only_when_stable=True,
        login_username="Artalus",
    )

    builder.add_common_builds()
    builder.run()
