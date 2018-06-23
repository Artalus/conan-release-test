from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="Artalus",
                                 channel='ci',
                                 remotes="https://api.bintray.com/conan/bincrafters/public-conan",
                                 build_policy='missing',

                                 upload="https://api.bintray.com/conan/artalus/conan-public",
                                 login_username="Artalus",
                                 stable_branch_pattern='release/*',
                                 )

    builder.add_common_builds()
    builder.conan_pip_package = 'conan==1.5.0.dev1'
    builder.run()
