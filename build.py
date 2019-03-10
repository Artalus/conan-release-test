#!/usr/bin/env python3
from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(\
        username="Artalus",
        channel='copato-dock',
        remotes="https://api.bintray.com/conan/bincrafters/public-conan",
        build_policy='missing',

        upload="https://api.bintray.com/conan/artalus/conan-public",
        stable_branch_pattern="release/*",
        upload_only_when_stable=True,
        login_username="Artalus",
    )

    builder.add_common_builds()
    builder.run()
