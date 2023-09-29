# Copyright (c) Meta Platforms, Inc. and affiliates.
# SPDX-License-Identifier: LGPL-2.1-or-later
# Generated by scripts/gen_dwarf_constants.py.

import enum
from typing import Text


class DW_ACCESS(enum.IntEnum):
    public = 0x1
    protected = 0x2
    private = 0x3

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_ACCESS_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_ADDR(enum.IntEnum):
    none = 0x0

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_ADDR_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_AT(enum.IntEnum):
    sibling = 0x1
    location = 0x2
    name = 0x3  # type: ignore
    ordering = 0x9
    subscr_data = 0xA
    byte_size = 0xB
    bit_offset = 0xC
    bit_size = 0xD
    element_list = 0xF
    stmt_list = 0x10
    low_pc = 0x11
    high_pc = 0x12
    language = 0x13
    member = 0x14
    discr = 0x15
    discr_value = 0x16
    visibility = 0x17
    import_ = 0x18
    string_length = 0x19
    common_reference = 0x1A
    comp_dir = 0x1B
    const_value = 0x1C
    containing_type = 0x1D
    default_value = 0x1E
    inline = 0x20
    is_optional = 0x21
    lower_bound = 0x22
    producer = 0x25
    prototyped = 0x27
    return_addr = 0x2A
    start_scope = 0x2C
    bit_stride = 0x2E
    stride_size = 0x2E
    upper_bound = 0x2F
    abstract_origin = 0x31
    accessibility = 0x32
    address_class = 0x33
    artificial = 0x34
    base_types = 0x35
    calling_convention = 0x36
    count = 0x37
    data_member_location = 0x38
    decl_column = 0x39
    decl_file = 0x3A
    decl_line = 0x3B
    declaration = 0x3C
    discr_list = 0x3D
    encoding = 0x3E
    external = 0x3F
    frame_base = 0x40
    friend = 0x41
    identifier_case = 0x42
    macro_info = 0x43
    namelist_item = 0x44
    priority = 0x45
    segment = 0x46
    specification = 0x47
    static_link = 0x48
    type = 0x49
    use_location = 0x4A
    variable_parameter = 0x4B
    virtuality = 0x4C
    vtable_elem_location = 0x4D
    allocated = 0x4E
    associated = 0x4F
    data_location = 0x50
    byte_stride = 0x51
    entry_pc = 0x52
    use_UTF8 = 0x53
    extension = 0x54
    ranges = 0x55
    trampoline = 0x56
    call_column = 0x57
    call_file = 0x58
    call_line = 0x59
    description = 0x5A
    binary_scale = 0x5B
    decimal_scale = 0x5C
    small = 0x5D
    decimal_sign = 0x5E
    digit_count = 0x5F
    picture_string = 0x60
    mutable = 0x61
    threads_scaled = 0x62
    explicit = 0x63
    object_pointer = 0x64
    endianity = 0x65
    elemental = 0x66
    pure = 0x67
    recursive = 0x68
    signature = 0x69
    main_subprogram = 0x6A
    data_bit_offset = 0x6B
    const_expr = 0x6C
    enum_class = 0x6D
    linkage_name = 0x6E
    string_length_bit_size = 0x6F
    string_length_byte_size = 0x70
    rank = 0x71
    str_offsets_base = 0x72
    addr_base = 0x73
    rnglists_base = 0x74
    dwo_id = 0x75
    dwo_name = 0x76
    reference = 0x77
    rvalue_reference = 0x78
    macros = 0x79
    call_all_calls = 0x7A
    call_all_source_calls = 0x7B
    call_all_tail_calls = 0x7C
    call_return_pc = 0x7D
    call_value = 0x7E
    call_origin = 0x7F
    call_parameter = 0x80
    call_pc = 0x81
    call_tail_call = 0x82
    call_target = 0x83
    call_target_clobbered = 0x84
    call_data_location = 0x85
    call_data_value = 0x86
    noreturn = 0x87
    alignment = 0x88
    export_symbols = 0x89
    deleted = 0x8A
    defaulted = 0x8B
    loclists_base = 0x8C
    ghs_namespace_alias = 0x806
    ghs_using_namespace = 0x807
    ghs_using_declaration = 0x808
    HP_block_index = 0x2000
    lo_user = 0x2000
    MIPS_fde = 0x2001
    MIPS_loop_begin = 0x2002
    MIPS_tail_loop_begin = 0x2003
    MIPS_epilog_begin = 0x2004
    MIPS_loop_unroll_factor = 0x2005
    MIPS_software_pipeline_depth = 0x2006
    MIPS_linkage_name = 0x2007
    MIPS_stride = 0x2008
    MIPS_abstract_name = 0x2009
    MIPS_clone_origin = 0x200A
    MIPS_has_inlines = 0x200B
    MIPS_stride_byte = 0x200C
    MIPS_stride_elem = 0x200D
    MIPS_ptr_dopetype = 0x200E
    MIPS_allocatable_dopetype = 0x200F
    MIPS_assumed_shape_dopetype = 0x2010
    MIPS_assumed_size = 0x2011
    HP_unmodifiable = 0x2001
    HP_prologue = 0x2005
    HP_epilogue = 0x2008
    HP_actuals_stmt_list = 0x2010
    HP_proc_per_section = 0x2011
    HP_raw_data_ptr = 0x2012
    HP_pass_by_reference = 0x2013
    HP_opt_level = 0x2014
    HP_prof_version_id = 0x2015
    HP_opt_flags = 0x2016
    HP_cold_region_low_pc = 0x2017
    HP_cold_region_high_pc = 0x2018
    HP_all_variables_modifiable = 0x2019
    HP_linkage_name = 0x201A
    HP_prof_flags = 0x201B
    HP_unit_name = 0x201F
    HP_unit_size = 0x2020
    HP_widened_byte_size = 0x2021
    HP_definition_points = 0x2022
    HP_default_location = 0x2023
    HP_is_result_param = 0x2029
    CPQ_discontig_ranges = 0x2001
    CPQ_semantic_events = 0x2002
    CPQ_split_lifetimes_var = 0x2003
    CPQ_split_lifetimes_rtn = 0x2004
    CPQ_prologue_length = 0x2005
    ghs_mangled = 0x2007
    ghs_rsm = 0x2083
    ghs_frsm = 0x2085
    ghs_frames = 0x2086
    ghs_rso = 0x2087
    ghs_subcpu = 0x2092
    ghs_lbrace_line = 0x2093
    INTEL_other_endian = 0x2026
    sf_names = 0x2101
    src_info = 0x2102
    mac_info = 0x2103
    src_coords = 0x2104
    body_begin = 0x2105
    body_end = 0x2106
    GNU_vector = 0x2107
    GNU_guarded_by = 0x2108
    GNU_pt_guarded_by = 0x2109
    GNU_guarded = 0x210A
    GNU_pt_guarded = 0x210B
    GNU_locks_excluded = 0x210C
    GNU_exclusive_locks_required = 0x210D
    GNU_shared_locks_required = 0x210E
    GNU_odr_signature = 0x210F
    GNU_template_name = 0x2110
    GNU_call_site_value = 0x2111
    GNU_call_site_data_value = 0x2112
    GNU_call_site_target = 0x2113
    GNU_call_site_target_clobbered = 0x2114
    GNU_tail_call = 0x2115
    GNU_all_tail_call_sites = 0x2116
    GNU_all_call_sites = 0x2117
    GNU_all_source_call_sites = 0x2118
    GNU_macros = 0x2119
    GNU_deleted = 0x211A
    GNU_dwo_name = 0x2130
    GNU_dwo_id = 0x2131
    GNU_ranges_base = 0x2132
    GNU_addr_base = 0x2133
    GNU_pubnames = 0x2134
    GNU_pubtypes = 0x2135
    GNU_discriminator = 0x2136
    GNU_locviews = 0x2137
    GNU_entry_view = 0x2138
    SUN_template = 0x2201
    VMS_rtnbeg_pd_address = 0x2201
    SUN_alignment = 0x2202
    SUN_vtable = 0x2203
    SUN_count_guarantee = 0x2204
    SUN_command_line = 0x2205
    SUN_vbase = 0x2206
    SUN_compile_options = 0x2207
    SUN_language = 0x2208
    SUN_browser_file = 0x2209
    SUN_vtable_abi = 0x2210
    SUN_func_offsets = 0x2211
    SUN_cf_kind = 0x2212
    SUN_vtable_index = 0x2213
    SUN_omp_tpriv_addr = 0x2214
    SUN_omp_child_func = 0x2215
    SUN_func_offset = 0x2216
    SUN_memop_type_ref = 0x2217
    SUN_profile_id = 0x2218
    SUN_memop_signature = 0x2219
    SUN_obj_dir = 0x2220
    SUN_obj_file = 0x2221
    SUN_original_name = 0x2222
    SUN_hwcprof_signature = 0x2223
    SUN_amd64_parmdump = 0x2224
    SUN_part_link_name = 0x2225
    SUN_link_name = 0x2226
    SUN_pass_with_const = 0x2227
    SUN_return_with_const = 0x2228
    SUN_import_by_name = 0x2229
    SUN_f90_pointer = 0x222A
    SUN_pass_by_ref = 0x222B
    SUN_f90_allocatable = 0x222C
    SUN_f90_assumed_shape_array = 0x222D
    SUN_c_vla = 0x222E
    SUN_return_value_ptr = 0x2230
    SUN_dtor_start = 0x2231
    SUN_dtor_length = 0x2232
    SUN_dtor_state_initial = 0x2233
    SUN_dtor_state_final = 0x2234
    SUN_dtor_state_deltas = 0x2235
    SUN_import_by_lname = 0x2236
    SUN_f90_use_only = 0x2237
    SUN_namelist_spec = 0x2238
    SUN_is_omp_child_func = 0x2239
    SUN_fortran_main_alias = 0x223A
    SUN_fortran_based = 0x223B
    ALTIUM_loclist = 0x2300
    use_GNAT_descriptive_type = 0x2301
    GNAT_descriptive_type = 0x2302
    GNU_numerator = 0x2303
    GNU_denominator = 0x2304
    GNU_bias = 0x2305
    go_kind = 0x2900
    go_key = 0x2901
    go_elem = 0x2902
    go_embedded_field = 0x2903
    go_runtime_type = 0x2904
    upc_threads_scaled = 0x3210
    IBM_wsa_addr = 0x393E
    IBM_home_location = 0x393F
    IBM_alt_srcview = 0x3940
    PGI_lbase = 0x3A00
    PGI_soffset = 0x3A01
    PGI_lstride = 0x3A02
    BORLAND_property_read = 0x3B11
    BORLAND_property_write = 0x3B12
    BORLAND_property_implements = 0x3B13
    BORLAND_property_index = 0x3B14
    BORLAND_property_default = 0x3B15
    BORLAND_Delphi_unit = 0x3B20
    BORLAND_Delphi_class = 0x3B21
    BORLAND_Delphi_record = 0x3B22
    BORLAND_Delphi_metaclass = 0x3B23
    BORLAND_Delphi_constructor = 0x3B24
    BORLAND_Delphi_destructor = 0x3B25
    BORLAND_Delphi_anonymous_method = 0x3B26
    BORLAND_Delphi_interface = 0x3B27
    BORLAND_Delphi_ABI = 0x3B28
    BORLAND_Delphi_frameptr = 0x3B30
    BORLAND_closure = 0x3B31
    LLVM_include_path = 0x3E00
    LLVM_config_macros = 0x3E01
    LLVM_sysroot = 0x3E02
    LLVM_tag_offset = 0x3E03
    LLVM_apinotes = 0x3E07
    LLVM_active_lane = 0x3E08
    LLVM_augmentation = 0x3E09
    LLVM_lanes = 0x3E0A
    LLVM_lane_pc = 0x3E0B
    LLVM_vector_size = 0x3E0C
    APPLE_optimized = 0x3FE1
    APPLE_flags = 0x3FE2
    APPLE_isa = 0x3FE3
    APPLE_block = 0x3FE4
    APPLE_major_runtime_vers = 0x3FE5
    APPLE_runtime_class = 0x3FE6
    APPLE_omit_frame_ptr = 0x3FE7
    APPLE_property_name = 0x3FE8
    APPLE_property_getter = 0x3FE9
    APPLE_property_setter = 0x3FEA
    APPLE_property_attribute = 0x3FEB
    APPLE_objc_complete_type = 0x3FEC
    APPLE_property = 0x3FED
    APPLE_objc_direct = 0x3FEE
    APPLE_sdk = 0x3FEF
    hi_user = 0x3FFF

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_AT_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_ATE(enum.IntEnum):
    address = 0x1
    boolean = 0x2
    complex_float = 0x3
    float = 0x4
    signed = 0x5
    signed_char = 0x6
    unsigned = 0x7
    unsigned_char = 0x8
    imaginary_float = 0x9
    packed_decimal = 0xA
    numeric_string = 0xB
    edited = 0xC
    signed_fixed = 0xD
    unsigned_fixed = 0xE
    decimal_float = 0xF
    UTF = 0x10
    UCS = 0x11
    ASCII = 0x12
    ALTIUM_fract = 0x80
    lo_user = 0x80
    ALTIUM_accum = 0x81
    HP_float80 = 0x80
    HP_complex_float80 = 0x81
    HP_float128 = 0x82
    HP_complex_float128 = 0x83
    HP_floathpintel = 0x84
    HP_imaginary_float80 = 0x85
    HP_imaginary_float128 = 0x86
    HP_VAX_float = 0x88
    HP_VAX_float_d = 0x89
    HP_packed_decimal = 0x8A
    HP_zoned_decimal = 0x8B
    HP_edited = 0x8C
    HP_signed_fixed = 0x8D
    HP_unsigned_fixed = 0x8E
    HP_VAX_complex_float = 0x8F
    HP_VAX_complex_float_d = 0x90
    SUN_interval_float = 0x91
    SUN_imaginary_float = 0x92
    hi_user = 0xFF

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_ATE_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_CC(enum.IntEnum):
    normal = 0x1
    program = 0x2
    nocall = 0x3
    pass_by_reference = 0x4
    pass_by_value = 0x5
    lo_user = 0x40
    GNU_renesas_sh = 0x40
    GNU_borland_fastcall_i386 = 0x41
    ALTIUM_interrupt = 0x65
    ALTIUM_near_system_stack = 0x66
    ALTIUM_near_user_stack = 0x67
    ALTIUM_huge_user_stack = 0x68
    GNU_BORLAND_safecall = 0xB0
    GNU_BORLAND_stdcall = 0xB1
    GNU_BORLAND_pascal = 0xB2
    GNU_BORLAND_msfastcall = 0xB3
    GNU_BORLAND_msreturn = 0xB4
    GNU_BORLAND_thiscall = 0xB5
    GNU_BORLAND_fastcall = 0xB6
    LLVM_vectorcall = 0xC0
    LLVM_Win64 = 0xC1
    LLVM_X86_64SysV = 0xC2
    LLVM_AAPCS = 0xC3
    LLVM_AAPCS_VFP = 0xC4
    LLVM_IntelOclBicc = 0xC5
    LLVM_SpirFunction = 0xC6
    LLVM_OpenCLKernel = 0xC7
    LLVM_Swift = 0xC8
    LLVM_PreserveMost = 0xC9
    LLVM_PreserveAll = 0xCA
    LLVM_X86RegCall = 0xCB
    GDB_IBM_OpenCL = 0xFF
    hi_user = 0xFF

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_CC_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_CFA(enum.IntEnum):
    advance_loc = 0x40
    offset = 0x80
    restore = 0xC0
    nop = 0x0
    set_loc = 0x1
    advance_loc1 = 0x2
    advance_loc2 = 0x3
    advance_loc4 = 0x4
    offset_extended = 0x5
    restore_extended = 0x6
    undefined = 0x7
    same_value = 0x8
    register = 0x9
    remember_state = 0xA
    restore_state = 0xB
    def_cfa = 0xC
    def_cfa_register = 0xD
    def_cfa_offset = 0xE
    def_cfa_expression = 0xF
    expression = 0x10
    offset_extended_sf = 0x11
    def_cfa_sf = 0x12
    def_cfa_offset_sf = 0x13
    val_offset = 0x14
    val_offset_sf = 0x15
    val_expression = 0x16
    lo_user = 0x1C
    MIPS_advance_loc8 = 0x1D
    GNU_window_save = 0x2D
    AARCH64_negate_ra_state = 0x2D
    GNU_args_size = 0x2E
    GNU_negative_offset_extended = 0x2F
    LLVM_def_aspace_cfa = 0x30
    LLVM_def_aspace_cfa_sf = 0x31
    METAWARE_info = 0x34
    hi_user = 0x3F

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_CFA_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_CHILDREN(enum.IntEnum):
    no = 0x0
    yes = 0x1

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_CHILDREN_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_DEFAULTED(enum.IntEnum):
    no = 0x0
    in_class = 0x1
    out_of_class = 0x2

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_DEFAULTED_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_DS(enum.IntEnum):
    unsigned = 0x1
    leading_overpunch = 0x2
    trailing_overpunch = 0x3
    leading_separate = 0x4
    trailing_separate = 0x5

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_DS_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_DSC(enum.IntEnum):
    label = 0x0
    range = 0x1

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_DSC_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_EH_PE(enum.IntEnum):
    absptr = 0x0
    uleb128 = 0x1
    udata2 = 0x2
    udata4 = 0x3
    udata8 = 0x4
    sleb128 = 0x9
    sdata2 = 0xA
    sdata4 = 0xB
    sdata8 = 0xC
    signed = 0x8
    pcrel = 0x10
    textrel = 0x20
    datarel = 0x30
    funcrel = 0x40
    aligned = 0x50
    indirect = 0x80
    omit = 0xFF

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_EH_PE_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_END(enum.IntEnum):
    default = 0x0
    big = 0x1
    little = 0x2
    lo_user = 0x40
    hi_user = 0xFF

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_END_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_FORM(enum.IntEnum):
    addr = 0x1
    block2 = 0x3
    block4 = 0x4
    data2 = 0x5
    data4 = 0x6
    data8 = 0x7
    string = 0x8
    block = 0x9
    block1 = 0xA
    data1 = 0xB
    flag = 0xC
    sdata = 0xD
    strp = 0xE
    udata = 0xF
    ref_addr = 0x10
    ref1 = 0x11
    ref2 = 0x12
    ref4 = 0x13
    ref8 = 0x14
    ref_udata = 0x15
    indirect = 0x16
    sec_offset = 0x17
    exprloc = 0x18
    flag_present = 0x19
    strx = 0x1A
    addrx = 0x1B
    ref_sup4 = 0x1C
    strp_sup = 0x1D
    data16 = 0x1E
    line_strp = 0x1F
    ref_sig8 = 0x20
    implicit_const = 0x21
    loclistx = 0x22
    rnglistx = 0x23
    ref_sup8 = 0x24
    strx1 = 0x25
    strx2 = 0x26
    strx3 = 0x27
    strx4 = 0x28
    addrx1 = 0x29
    addrx2 = 0x2A
    addrx3 = 0x2B
    addrx4 = 0x2C
    GNU_addr_index = 0x1F01
    GNU_str_index = 0x1F02
    GNU_ref_alt = 0x1F20
    GNU_strp_alt = 0x1F21
    LLVM_addrx_offset = 0x2001

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_FORM_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_ID(enum.IntEnum):
    case_sensitive = 0x0
    up_case = 0x1
    down_case = 0x2
    case_insensitive = 0x3

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_ID_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_IDX(enum.IntEnum):
    compile_unit = 0x1
    type_unit = 0x2
    die_offset = 0x3
    parent = 0x4
    type_hash = 0x5
    GNU_internal = 0x2000
    lo_user = 0x2000
    GNU_external = 0x2001
    hi_user = 0x3FFF

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_IDX_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_INL(enum.IntEnum):
    not_inlined = 0x0
    inlined = 0x1
    declared_not_inlined = 0x2
    declared_inlined = 0x3

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_INL_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_LANG(enum.IntEnum):
    C89 = 0x1
    C = 0x2
    Ada83 = 0x3
    C_plus_plus = 0x4
    Cobol74 = 0x5
    Cobol85 = 0x6
    Fortran77 = 0x7
    Fortran90 = 0x8
    Pascal83 = 0x9
    Modula2 = 0xA
    Java = 0xB
    C99 = 0xC
    Ada95 = 0xD
    Fortran95 = 0xE
    PLI = 0xF
    ObjC = 0x10
    ObjC_plus_plus = 0x11
    UPC = 0x12
    D = 0x13
    Python = 0x14
    OpenCL = 0x15
    Go = 0x16
    Modula3 = 0x17
    Haskell = 0x18
    C_plus_plus_03 = 0x19
    C_plus_plus_11 = 0x1A
    OCaml = 0x1B
    Rust = 0x1C
    C11 = 0x1D
    Swift = 0x1E
    Julia = 0x1F
    Dylan = 0x20
    C_plus_plus_14 = 0x21
    Fortran03 = 0x22
    Fortran08 = 0x23
    RenderScript = 0x24
    BLISS = 0x25
    Kotlin = 0x26
    Zig = 0x27
    Crystal = 0x28
    C_plus_plus_17 = 0x2A
    C_plus_plus_20 = 0x2B
    C17 = 0x2C
    Fortran18 = 0x2D
    Ada2005 = 0x2E
    Ada2012 = 0x2F
    HIP = 0x30
    Assembly = 0x31
    C_sharp = 0x32
    Mojo = 0x33
    lo_user = 0x8000
    Mips_Assembler = 0x8001
    Upc = 0x8765
    GOOGLE_RenderScript = 0x8E57
    ALTIUM_Assembler = 0x9101
    BORLAND_Delphi = 0xB000
    SUN_Assembler = 0x9001
    hi_user = 0xFFFF

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_LANG_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_LLE(enum.IntEnum):
    end_of_list = 0x0
    base_addressx = 0x1
    startx_endx = 0x2
    startx_length = 0x3
    offset_pair = 0x4
    default_location = 0x5
    base_address = 0x6
    start_end = 0x7
    start_length = 0x8

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_LLE_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_LNCT(enum.IntEnum):
    path = 0x1
    directory_index = 0x2
    timestamp = 0x3
    size = 0x4
    MD5 = 0x5
    GNU_subprogram_name = 0x6
    GNU_decl_file = 0x7
    GNU_decl_line = 0x8
    lo_user = 0x2000
    LLVM_source = 0x2001
    LLVM_is_MD5 = 0x2002
    hi_user = 0x3FFF

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_LNCT_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_LNE(enum.IntEnum):
    end_sequence = 0x1
    set_address = 0x2
    define_file = 0x3
    set_discriminator = 0x4
    HP_negate_is_UV_update = 0x11
    HP_push_context = 0x12
    HP_pop_context = 0x13
    HP_set_file_line_column = 0x14
    HP_set_routine_name = 0x15
    HP_set_sequence = 0x16
    HP_negate_post_semantics = 0x17
    HP_negate_function_exit = 0x18
    HP_negate_front_end_logical = 0x19
    HP_define_proc = 0x20
    HP_source_file_correlation = 0x80
    lo_user = 0x80
    hi_user = 0xFF

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_LNE_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_LNS(enum.IntEnum):
    copy = 0x1
    advance_pc = 0x2
    advance_line = 0x3
    set_file = 0x4
    set_column = 0x5
    negate_stmt = 0x6
    set_basic_block = 0x7
    const_add_pc = 0x8
    fixed_advance_pc = 0x9
    set_prologue_end = 0xA
    set_epilogue_begin = 0xB
    set_isa = 0xC
    set_address_from_logical = 0xD
    set_subprogram = 0xD
    inlined_call = 0xE
    pop_context = 0xF

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_LNS_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_MACINFO(enum.IntEnum):
    define = 0x1
    undef = 0x2
    start_file = 0x3
    end_file = 0x4
    vendor_ext = 0xFF

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_MACINFO_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_MACRO(enum.IntEnum):
    define = 0x1
    undef = 0x2
    start_file = 0x3
    end_file = 0x4
    define_strp = 0x5
    undef_strp = 0x6
    import_ = 0x7
    define_sup = 0x8
    undef_sup = 0x9
    import_sup = 0xA
    define_strx = 0xB
    undef_strx = 0xC
    lo_user = 0xE0
    hi_user = 0xFF

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_MACRO_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_OP(enum.IntEnum):
    addr = 0x3
    deref = 0x6
    const1u = 0x8
    const1s = 0x9
    const2u = 0xA
    const2s = 0xB
    const4u = 0xC
    const4s = 0xD
    const8u = 0xE
    const8s = 0xF
    constu = 0x10
    consts = 0x11
    dup = 0x12
    drop = 0x13
    over = 0x14
    pick = 0x15
    swap = 0x16
    rot = 0x17
    xderef = 0x18
    abs = 0x19
    and_ = 0x1A
    div = 0x1B
    minus = 0x1C
    mod = 0x1D
    mul = 0x1E
    neg = 0x1F
    not_ = 0x20
    or_ = 0x21
    plus = 0x22
    plus_uconst = 0x23
    shl = 0x24
    shr = 0x25
    shra = 0x26
    xor = 0x27
    bra = 0x28
    eq = 0x29
    ge = 0x2A
    gt = 0x2B
    le = 0x2C
    lt = 0x2D
    ne = 0x2E
    skip = 0x2F
    lit0 = 0x30
    lit1 = 0x31
    lit2 = 0x32
    lit3 = 0x33
    lit4 = 0x34
    lit5 = 0x35
    lit6 = 0x36
    lit7 = 0x37
    lit8 = 0x38
    lit9 = 0x39
    lit10 = 0x3A
    lit11 = 0x3B
    lit12 = 0x3C
    lit13 = 0x3D
    lit14 = 0x3E
    lit15 = 0x3F
    lit16 = 0x40
    lit17 = 0x41
    lit18 = 0x42
    lit19 = 0x43
    lit20 = 0x44
    lit21 = 0x45
    lit22 = 0x46
    lit23 = 0x47
    lit24 = 0x48
    lit25 = 0x49
    lit26 = 0x4A
    lit27 = 0x4B
    lit28 = 0x4C
    lit29 = 0x4D
    lit30 = 0x4E
    lit31 = 0x4F
    reg0 = 0x50
    reg1 = 0x51
    reg2 = 0x52
    reg3 = 0x53
    reg4 = 0x54
    reg5 = 0x55
    reg6 = 0x56
    reg7 = 0x57
    reg8 = 0x58
    reg9 = 0x59
    reg10 = 0x5A
    reg11 = 0x5B
    reg12 = 0x5C
    reg13 = 0x5D
    reg14 = 0x5E
    reg15 = 0x5F
    reg16 = 0x60
    reg17 = 0x61
    reg18 = 0x62
    reg19 = 0x63
    reg20 = 0x64
    reg21 = 0x65
    reg22 = 0x66
    reg23 = 0x67
    reg24 = 0x68
    reg25 = 0x69
    reg26 = 0x6A
    reg27 = 0x6B
    reg28 = 0x6C
    reg29 = 0x6D
    reg30 = 0x6E
    reg31 = 0x6F
    breg0 = 0x70
    breg1 = 0x71
    breg2 = 0x72
    breg3 = 0x73
    breg4 = 0x74
    breg5 = 0x75
    breg6 = 0x76
    breg7 = 0x77
    breg8 = 0x78
    breg9 = 0x79
    breg10 = 0x7A
    breg11 = 0x7B
    breg12 = 0x7C
    breg13 = 0x7D
    breg14 = 0x7E
    breg15 = 0x7F
    breg16 = 0x80
    breg17 = 0x81
    breg18 = 0x82
    breg19 = 0x83
    breg20 = 0x84
    breg21 = 0x85
    breg22 = 0x86
    breg23 = 0x87
    breg24 = 0x88
    breg25 = 0x89
    breg26 = 0x8A
    breg27 = 0x8B
    breg28 = 0x8C
    breg29 = 0x8D
    breg30 = 0x8E
    breg31 = 0x8F
    regx = 0x90
    fbreg = 0x91
    bregx = 0x92
    piece = 0x93
    deref_size = 0x94
    xderef_size = 0x95
    nop = 0x96
    push_object_address = 0x97
    call2 = 0x98
    call4 = 0x99
    call_ref = 0x9A
    form_tls_address = 0x9B
    call_frame_cfa = 0x9C
    bit_piece = 0x9D
    implicit_value = 0x9E
    stack_value = 0x9F
    implicit_pointer = 0xA0
    addrx = 0xA1
    constx = 0xA2
    entry_value = 0xA3
    const_type = 0xA4
    regval_type = 0xA5
    deref_type = 0xA6
    xderef_type = 0xA7
    convert = 0xA8
    reinterpret = 0xA9
    GNU_push_tls_address = 0xE0
    WASM_location = 0xED
    WASM_location_int = 0xEE
    lo_user = 0xE0
    LLVM_form_aspace_address = 0xE1
    LLVM_push_lane = 0xE2
    LLVM_offset = 0xE3
    LLVM_offset_uconst = 0xE4
    LLVM_bit_offset = 0xE5
    LLVM_call_frame_entry_reg = 0xE6
    LLVM_undefined = 0xE7
    LLVM_aspace_bregx = 0xE8
    LLVM_aspace_implicit_pointer = 0xE9
    LLVM_piece_end = 0xEA
    LLVM_extend = 0xEB
    LLVM_select_bit_piece = 0xEC
    HP_unknown = 0xE0
    HP_is_value = 0xE1
    HP_fltconst4 = 0xE2
    HP_fltconst8 = 0xE3
    HP_mod_range = 0xE4
    HP_unmod_range = 0xE5
    HP_tls = 0xE6
    INTEL_bit_piece = 0xE8
    GNU_uninit = 0xF0
    APPLE_uninit = 0xF0
    GNU_encoded_addr = 0xF1
    GNU_implicit_pointer = 0xF2
    GNU_entry_value = 0xF3
    GNU_const_type = 0xF4
    GNU_regval_type = 0xF5
    GNU_deref_type = 0xF6
    GNU_convert = 0xF7
    GNU_reinterpret = 0xF9
    GNU_parameter_ref = 0xFA
    GNU_addr_index = 0xFB
    GNU_const_index = 0xFC
    GNU_variable_value = 0xFD
    PGI_omp_thread_num = 0xF8
    hi_user = 0xFF

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_OP_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_ORD(enum.IntEnum):
    row_major = 0x0
    col_major = 0x1

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_ORD_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_RLE(enum.IntEnum):
    end_of_list = 0x0
    base_addressx = 0x1
    startx_endx = 0x2
    startx_length = 0x3
    offset_pair = 0x4
    base_address = 0x5
    start_end = 0x6
    start_length = 0x7

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_RLE_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_SECT(enum.IntEnum):
    INFO = 0x1
    TYPES = 0x2
    ABBREV = 0x3
    LINE = 0x4
    LOCLISTS = 0x5
    STR_OFFSETS = 0x6
    MACRO = 0x7
    RNGLISTS = 0x8

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_SECT_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_TAG(enum.IntEnum):
    array_type = 0x1
    class_type = 0x2
    entry_point = 0x3
    enumeration_type = 0x4
    formal_parameter = 0x5
    imported_declaration = 0x8
    label = 0xA
    lexical_block = 0xB
    member = 0xD
    pointer_type = 0xF
    reference_type = 0x10
    compile_unit = 0x11
    string_type = 0x12
    structure_type = 0x13
    subroutine_type = 0x15
    typedef = 0x16
    union_type = 0x17
    unspecified_parameters = 0x18
    variant = 0x19
    common_block = 0x1A
    common_inclusion = 0x1B
    inheritance = 0x1C
    inlined_subroutine = 0x1D
    module = 0x1E
    ptr_to_member_type = 0x1F
    set_type = 0x20
    subrange_type = 0x21
    with_stmt = 0x22
    access_declaration = 0x23
    base_type = 0x24
    catch_block = 0x25
    const_type = 0x26
    constant = 0x27
    enumerator = 0x28
    file_type = 0x29
    friend = 0x2A
    namelist = 0x2B
    namelist_item = 0x2C
    packed_type = 0x2D
    subprogram = 0x2E
    template_type_parameter = 0x2F
    template_value_parameter = 0x30
    thrown_type = 0x31
    try_block = 0x32
    variant_part = 0x33
    variable = 0x34
    volatile_type = 0x35
    dwarf_procedure = 0x36
    restrict_type = 0x37
    interface_type = 0x38
    namespace = 0x39
    imported_module = 0x3A
    unspecified_type = 0x3B
    partial_unit = 0x3C
    imported_unit = 0x3D
    mutable_type = 0x3E
    condition = 0x3F
    shared_type = 0x40
    type_unit = 0x41
    rvalue_reference_type = 0x42
    template_alias = 0x43
    coarray_type = 0x44
    generic_subrange = 0x45
    dynamic_type = 0x46
    atomic_type = 0x47
    call_site = 0x48
    call_site_parameter = 0x49
    skeleton_unit = 0x4A
    immutable_type = 0x4B
    lo_user = 0x4080
    MIPS_loop = 0x4081
    HP_array_descriptor = 0x4090
    format_label = 0x4101
    function_template = 0x4102
    class_template = 0x4103
    GNU_BINCL = 0x4104
    GNU_EINCL = 0x4105
    GNU_template_template_param = 0x4106
    GNU_template_parameter_pack = 0x4107
    GNU_formal_parameter_pack = 0x4108
    GNU_call_site = 0x4109
    GNU_call_site_parameter = 0x410A
    SUN_function_template = 0x4201
    SUN_class_template = 0x4202
    SUN_struct_template = 0x4203
    SUN_union_template = 0x4204
    SUN_indirect_inheritance = 0x4205
    SUN_codeflags = 0x4206
    SUN_memop_info = 0x4207
    SUN_omp_child_func = 0x4208
    SUN_rtti_descriptor = 0x4209
    SUN_dtor_info = 0x420A
    SUN_dtor = 0x420B
    SUN_f90_interface = 0x420C
    SUN_fortran_vax_structure = 0x420D
    SUN_hi = 0x42FF
    ALTIUM_circ_type = 0x5101
    ALTIUM_mwa_circ_type = 0x5102
    ALTIUM_rev_carry_type = 0x5103
    ALTIUM_rom = 0x5111
    LLVM_annotation = 0x6000
    ghs_namespace = 0x8004
    ghs_using_namespace = 0x8005
    ghs_using_declaration = 0x8006
    ghs_template_templ_param = 0x8007
    upc_shared_type = 0x8765
    upc_strict_type = 0x8766
    upc_relaxed_type = 0x8767
    PGI_kanji_type = 0xA000
    PGI_interface_block = 0xA020
    BORLAND_property = 0xB000
    BORLAND_Delphi_string = 0xB001
    BORLAND_Delphi_dynamic_array = 0xB002
    BORLAND_Delphi_set = 0xB003
    BORLAND_Delphi_variant = 0xB004
    hi_user = 0xFFFF

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_TAG_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_UT(enum.IntEnum):
    compile = 0x1
    type = 0x2
    partial = 0x3
    skeleton = 0x4
    split_compile = 0x5
    split_type = 0x6
    lo_user = 0x80
    hi_user = 0xFF

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_UT_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_VIRTUALITY(enum.IntEnum):
    none = 0x0
    virtual = 0x1
    pure_virtual = 0x2

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_VIRTUALITY_{cls(value).name}"
        except ValueError:
            return hex(value)


class DW_VIS(enum.IntEnum):
    local = 0x1
    exported = 0x2
    qualified = 0x3

    @classmethod
    def str(cls, value: int) -> Text:
        try:
            return f"DW_VIS_{cls(value).name}"
        except ValueError:
            return hex(value)
