
from decimal import Decimal
from model_mommy import mommy

from django.test import TestCase

from pdbdrop.models import Upload
from pdbdrop.use_cases import SpawnPdb2MovieProcessUseCase


class SpawnPdb2MovieProcessUseCaseTests(TestCase):

    def setUp(self):
        self.use_case = SpawnPdb2MovieProcessUseCase

    def test_empty_options_return_simple_string(self):
        upload_model = mommy.make(Upload)
        use_case = self.use_case(upload_model=upload_model)
        self.assertEqual(
            'python pdb2movie.py ' + upload_model.file_path + ' ',
            use_case.execute()
        )

    def test_keep_list_option(self):
        upload_model = mommy.make(Upload, keep_list='1 2 3')
        use_case = self.use_case(upload_model=upload_model)
        self.assertEqual(
            'python pdb2movie.py ' + upload_model.file_path + ' --keep ' + upload_model.keep_list + ' ',
            use_case.execute()
        )

    def test_waters_option(self):
        upload_model = mommy.make(Upload, waters=True)
        use_case = self.use_case(upload_model=upload_model)
        self.assertEqual(
            'python pdb2movie.py ' + upload_model.file_path + ' --waters ',
            use_case.execute()
        )

    def test_confs_option(self):
        upload_model = mommy.make(Upload, confs=1)
        use_case = self.use_case(upload_model=upload_model)
        self.assertEqual(
            'python pdb2movie.py ' + upload_model.file_path + ' --confs ' + str(upload_model.confs) + ' ',
            use_case.execute()
        )

    def test_freq_option(self):
        upload_model = mommy.make(Upload, freq=1)
        use_case = self.use_case(upload_model=upload_model)
        self.assertEqual(
            'python pdb2movie.py ' + upload_model.file_path + ' --freq ' + str(upload_model.freq) + ' ',
            use_case.execute()
        )

    def test_step_option(self):
        upload_model = Upload(id='2222', file_path='lalala', user_email="a@b.com", step=Decimal('11.1'))
        use_case = self.use_case(upload_model=upload_model)
        self.assertEqual(
            'python pdb2movie.py ' + upload_model.file_path + ' --step ' + str(upload_model.step) + ' ',
            use_case.execute()
        )
        upload_model.delete()

    def test_dstep_option(self):
        upload_model = Upload(id='2222', file_path='lalala', user_email="a@b.com", dstep=Decimal('11.1'))
        use_case = self.use_case(upload_model=upload_model)
        self.assertEqual(
            'python pdb2movie.py ' + upload_model.file_path + ' --dstep ' + str(upload_model.dstep) + ' ',
            use_case.execute()
        )
        upload_model.delete()

    def test_res_option(self):
        upload_model = Upload(id='2222', file_path='lalala', user_email="a@b.com", res=[1, 2, 3])
        use_case = self.use_case(upload_model=upload_model)
        self.assertEqual(
            'python pdb2movie.py ' + upload_model.file_path + ' --res ' + str(upload_model.res[0]) + ' ' + str(upload_model.res[1]) + ' ',
            use_case.execute()
        )
        upload_model.delete()

    def test_modes_option(self):
        upload_model = Upload(id='2222', file_path='lalala', user_email="a@b.com", modes=[1, 2, 3])
        use_case = self.use_case(upload_model=upload_model)
        self.assertEqual(
            'python pdb2movie.py ' + upload_model.file_path + ' --modes ' + str(upload_model.modes[0]) + ' ' + str(upload_model.modes[1]) + ' ' + str(upload_model.modes[2]) + ' ',
            use_case.execute()
        )
        upload_model.delete()

    def test_ecuts_option(self):
        upload_model = Upload(id='2222', file_path='lalala', user_email="a@b.com", ecuts="11.1 22.2 33.3")
        use_case = self.use_case(upload_model=upload_model)
        self.assertEqual(
            'python pdb2movie.py ' + upload_model.file_path + ' --ecuts ' + upload_model.ecuts + ' ',
            use_case.execute()
        )
        upload_model.delete()

    def test_three_d_option(self):
        upload_model = mommy.make(Upload, three_d=True)
        use_case = self.use_case(upload_model=upload_model)
        self.assertEqual(
            'python pdb2movie.py ' + upload_model.file_path + ' --threed ',
            use_case.execute()
        )

    def test_combi_option(self):
        upload_model = mommy.make(Upload, combi=True)
        use_case = self.use_case(upload_model=upload_model)
        self.assertEqual(
            'python pdb2movie.py ' + upload_model.file_path + ' --combi ',
            use_case.execute()
        )

    def test_multiple_option(self):
        upload_model = mommy.make(Upload, multiple=True)
        use_case = self.use_case(upload_model=upload_model)
        self.assertEqual(
            'python pdb2movie.py ' + upload_model.file_path + ' --multiple ',
            use_case.execute()
        )

    def test_video_option(self):
        upload_model = mommy.make(Upload, video_path='lalala')
        use_case = self.use_case(upload_model=upload_model)
        self.assertEqual(
            'python pdb2movie.py ' + upload_model.file_path + ' --video lalala ',
            use_case.execute()
        )

    def test_all_options(self):
        upload_model = Upload(
            id='2222',
            file_path='lalala',
            keep_list='keep',
            waters=True,
            confs=1,
            freq=2,
            step=Decimal(33.3),
            dstep=Decimal(44.4),
            res=[1, 2, 4],
            modes=[1, 2],
            ecuts="11.1 22.2",
            three_d=True,
            combi=True,
            multiple=True,
            video_path="lululu",
            user_email="a@b.com"
        )

        use_case = self.use_case(upload_model=upload_model)

        self.assertEqual(
            'python pdb2movie.py ' + upload_model.file_path + ' --keep ' + upload_model.keep_list + ' --waters --confs ' + str(upload_model.confs) + ' --freq ' + str(upload_model.freq) + ' --step ' + str(upload_model.step) + ' --dstep ' + str(upload_model.dstep) + ' --res ' + str(upload_model.res[0]) + ' ' + str(upload_model.res[1]) + ' --modes ' + str(upload_model.modes[0]) + ' ' + str(upload_model.modes[1]) + ' --ecuts ' + upload_model.ecuts + ' --threed --combi --multiple --video ' + upload_model.video_path + ' ',
            use_case.execute()
        )
