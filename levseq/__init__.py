###############################################################################
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################

__title__ = 'levseq'
__description__ = 'LevSeq nanopore sequencing'
__url__ = 'https://github.com/fhalab/levseq/'
__version__ = '1.5.1'
__author__ = 'Yueming Long, Ariane Mora, Francesca-Zhoufan Li, Emre Gursoy'
__author_email__ = 'ylong@caltech.edu'
__license__ = 'GPL3'

from importlib import import_module
import sys as _sys


_LAZY_MODULES = {
    'cmd': 'levseq.cmd',
    'filter_orientation': 'levseq.filter_orientation',
    'globals': 'levseq.globals',
    'interface': 'levseq.interface',
    'run_levseq': 'levseq.run_levseq',
    'simulation': 'levseq.simulation',
    'user': 'levseq.user',
    'utils': 'levseq.utils',
    'variantcaller': 'levseq.variantcaller',
    'visualization': 'levseq.visualization',
}

_LAZY_EXPORTS = {
    'ALL_AAS': 'levseq.variantcaller',
    'AlignIO': 'levseq.visualization',
    'CODONS': 'levseq.globals',
    'CWD': 'levseq.interface',
    'ColumnDataSource': 'levseq.visualization',
    'Counter': 'levseq.visualization',
    'CustomJS': 'levseq.visualization',
    'DEFAULT_TARGETS': 'levseq.globals',
    'Div': 'levseq.visualization',
    'FactorRange': 'levseq.visualization',
    'HoverTool': 'levseq.visualization',
    'Label': 'levseq.visualization',
    'Legend': 'levseq.visualization',
    'LegendItem': 'levseq.visualization',
    'Motif': 'levseq.visualization',
    'MultipleSeqAlignment': 'levseq.visualization',
    'NUC_COLOR_DICT': 'levseq.visualization',
    'PCA': 'levseq.user',
    'Path': 'levseq.variantcaller',
    'Range1d': 'levseq.visualization',
    'RangeSlider': 'levseq.visualization',
    'Rect': 'levseq.visualization',
    'SCORE_MATRIX': 'levseq.globals',
    'SW_ALIGN_PARAMS': 'levseq.globals',
    'SciUtil': 'levseq.user',
    'Seq': 'levseq.filter_orientation',
    'SeqIO': 'levseq.variantcaller',
    'Spacer': 'levseq.visualization',
    'Tap': 'levseq.visualization',
    'TapTool': 'levseq.visualization',
    'Text': 'levseq.visualization',
    'ThreadPool': 'levseq.variantcaller',
    'ThreadPoolExecutor': 'levseq.filter_orientation',
    'VariantCaller': 'levseq.variantcaller',
    'WELL_IDS': 'levseq.visualization',
    'aa1': 'levseq.variantcaller',
    'aa_to_index': 'levseq.user',
    'aggregate_conservation': 'levseq.visualization',
    'aggregate_gray_blocks': 'levseq.visualization',
    'alignment_from_cigar': 'levseq.variantcaller',
    'amino_acid_to_codon': 'levseq.variantcaller',
    'amino_acids': 'levseq.user',
    'annotations': 'levseq.visualization',
    'argparse': 'levseq.interface',
    'as_completed': 'levseq.filter_orientation',
    'basecall_model': 'levseq.interface',
    'binomtest': 'levseq.variantcaller',
    'build_cli_parser': 'levseq.interface',
    'build_kmer_set': 'levseq.filter_orientation',
    'calc_mutation_significance_for_position_in_well': 'levseq.variantcaller',
    'calculate_mutation_significance_across_well': 'levseq.variantcaller',
    'cc': 'levseq.visualization',
    'check_demultiplexing': 'levseq.variantcaller',
    'check_variants': 'levseq.simulation',
    'column': 'levseq.visualization',
    'combine_pvalues': 'levseq.variantcaller',
    'combine_seq_func_data': 'levseq.interface',
    'convert_variant_df_to_seqs': 'levseq.user',
    'count_kmer_hits': 'levseq.filter_orientation',
    'deepcopy': 'levseq.variantcaller',
    'defaultdict': 'levseq.variantcaller',
    'execute_LevSeq': 'levseq.interface',
    'figure': 'levseq.visualization',
    'filter_demultiplexed_folder': 'levseq.filter_orientation',
    'filter_single_file': 'levseq.filter_orientation',
    'generate_epcr_library': 'levseq.simulation',
    'generate_platemaps': 'levseq.visualization',
    'generate_ssm_library': 'levseq.simulation',
    'get_colour': 'levseq.user',
    'get_cons': 'levseq.visualization',
    'get_cons_diff_colorNseq': 'levseq.visualization',
    'get_cons_seq': 'levseq.visualization',
    'get_dummy_plate_df': 'levseq.variantcaller',
    'get_mut': 'levseq.variantcaller',
    'get_reads_for_well': 'levseq.variantcaller',
    'get_sequence_colors': 'levseq.visualization',
    'get_sequence_diff_colorNseq': 'levseq.visualization',
    'get_template_df': 'levseq.variantcaller',
    'get_variant_label_for_well': 'levseq.variantcaller',
    'get_well_ids': 'levseq.visualization',
    'glob': 'levseq.variantcaller',
    'gridplot': 'levseq.visualization',
    'gzip': 'levseq.filter_orientation',
    'hv': 'levseq.visualization',
    'init_notebook_env': 'levseq.visualization',
    'insert_nt': 'levseq.simulation',
    'iter_fastq_records': 'levseq.filter_orientation',
    'logger': 'levseq.variantcaller',
    'logging': 'levseq.variantcaller',
    'main': 'levseq.cmd',
    'make_epcr_de_experiment': 'levseq.simulation',
    'make_experiment': 'levseq.simulation',
    'make_mixed_well_epcr_de_experiment': 'levseq.simulation',
    'make_msa': 'levseq.user',
    'make_oligopool_plates': 'levseq.visualization',
    'make_pca': 'levseq.user',
    'make_row_from_read_pileup_across_well': 'levseq.variantcaller',
    'make_ssm_de_experiment': 'levseq.simulation',
    'make_well_df_for_saving': 'levseq.simulation',
    'make_well_df_from_reads': 'levseq.variantcaller',
    'match_color': 'levseq.visualization',
    'math': 'levseq.variantcaller',
    'min_depth': 'levseq.interface',
    'mpl': 'levseq.visualization',
    'multipletests': 'levseq.variantcaller',
    'mutate_sequence': 'levseq.simulation',
    'np': 'levseq.variantcaller',
    'ns': 'levseq.visualization',
    'one_hot_encode': 'levseq.user',
    'os': 'levseq.variantcaller',
    'output_file': 'levseq.visualization',
    'output_notebook': 'levseq.visualization',
    'padding_end': 'levseq.interface',
    'padding_start': 'levseq.interface',
    'pd': 'levseq.variantcaller',
    'plot_empty': 'levseq.visualization',
    'plot_seaborn_heatmap': 'levseq.visualization',
    'plot_sequence_alignment': 'levseq.visualization',
    'plt': 'levseq.visualization',
    'pn': 'levseq.visualization',
    'postprocess_variant_df': 'levseq.variantcaller',
    'pysam': 'levseq.variantcaller',
    'random': 'levseq.variantcaller',
    're': 'levseq.variantcaller',
    'row': 'levseq.visualization',
    'run_LevSeq': 'levseq.interface',
    'sample_kmer_positions': 'levseq.filter_orientation',
    'save': 'levseq.visualization',
    'show': 'levseq.visualization',
    'shutil': 'levseq.variantcaller',
    'sns': 'levseq.visualization',
    'subprocess': 'levseq.variantcaller',
    'sys': 'levseq.visualization',
    'threshold': 'levseq.interface',
    'tqdm': 'levseq.variantcaller',
    'translate': 'levseq.variantcaller',
    'u': 'levseq.user',
    'warnings': 'levseq.variantcaller',
    'well2nb': 'levseq.visualization',
    'write_msa_for_df': 'levseq.simulation',
}

__all__ = [
    '__title__',
    '__description__',
    '__url__',
    '__version__',
    '__author__',
    '__author_email__',
    '__license__',
    *sorted(_LAZY_MODULES),
    *sorted(_LAZY_EXPORTS),
]


def __getattr__(name):
    if name in _LAZY_MODULES:
        module = import_module(_LAZY_MODULES[name])
        vars(_sys.modules[__name__])[name] = module
        return module

    if name in _LAZY_EXPORTS:
        module = import_module(_LAZY_EXPORTS[name])
        value = getattr(module, name)
        vars(_sys.modules[__name__])[name] = value
        return value

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return sorted(set(vars(_sys.modules[__name__])) | set(__all__))
