def test_file_exists(host):
    smallstep_ca = host.file('/smallstep_ca.yml')
    assert smallstep_ca.exists
    assert smallstep_ca.contains('your')

# def test_smallstep_ca_is_installed(host):
#     smallstep_ca = host.package('smallstep_ca')
#     assert smallstep_ca.is_installed
#
#
# def test_user_and_group_exist(host):
#     user = host.user('smallstep_ca')
#     assert user.group == 'smallstep_ca'
#     assert user.home == '/var/lib/smallstep_ca'
#
#
# def test_service_is_running_and_enabled(host):
#     smallstep_ca = host.service('smallstep_ca')
#     assert smallstep_ca.is_enabled
#     assert smallstep_ca.is_running
