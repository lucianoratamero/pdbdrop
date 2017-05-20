

class SpawnPdb2MovieProcessUseCase(object):

    def __init__(self, upload_model):
        self.upload_model = upload_model

    def execute(self):
        options = ' '

        if self.upload_model.keep_list:
            options += '--keep ' + self.upload_model.keep_list + ' '

        if self.upload_model.waters:
            options += '--waters '

        if self.upload_model.confs:
            options += '--confs ' + str(self.upload_model.confs) + ' '

        if self.upload_model.freq:
            options += '--freq ' + str(self.upload_model.freq) + ' '

        if self.upload_model.step:
            options += '--step ' + str(self.upload_model.step) + ' '

        if self.upload_model.dstep:
            options += '--dstep ' + str(self.upload_model.dstep) + ' '

        if self.upload_model.res:
            options += '--res ' + str(self.upload_model.res[0]) + ' ' + str(self.upload_model.res[1]) + ' '

        if self.upload_model.modes:
            options += '--modes '
            for number in self.upload_model.modes:
                options += str(number) + ' '

        if self.upload_model.ecuts:
            options += '--ecuts ' + self.upload_model.ecuts + ' '

        if self.upload_model.three_d:
            options += '--threed '

        if self.upload_model.combi:
            options += '--combi '

        if self.upload_model.multiple:
            options += '--multiple '

        if self.upload_model.video_path:
            options += '--video ' + self.upload_model.video_path + ' '

        return 'python pdb2movie.py ' + self.upload_model.file_path + options
